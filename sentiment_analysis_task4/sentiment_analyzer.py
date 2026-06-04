# sentiment_analyzer.py - FOR LARGE AMAZON REVIEWS FILE
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotions(text):
    if not isinstance(text, str):
        return "neutral", {}
    
    text_lower = text.lower()
    
    emotions = {
        'joy': ['love', 'great', 'perfect', 'amazing', 'happy', 'awesome', 'wonderful', 'excellent', 'best', 'obsessed', 'excited', 'fantastic', 'incredible'],
        'anger': ['terrible', 'hate', 'awful', 'bad', 'horrible', 'angry', 'furious', 'worst', 'broke', 'frustrating', 'dangerous', 'disgusting'],
        'sadness': ['sad', 'disappointed', 'unfortunate', 'sorry', 'regret', 'unhappy', 'lost'],
        'fear': ['worried', 'scared', 'afraid', 'nervous', 'anxious', 'fear'],
        'surprise': ['surprised', 'unexpected', 'wow', 'shocked'],
        'trust': ['good', 'reliable', 'honest', 'trust', 'fair', 'recommend', 'decent', 'works', 'fine']
    }
    
    scores = {}
    for emotion, keywords in emotions.items():
        count = 0
        for keyword in keywords:
            if keyword in text_lower:
                count += 1
        scores[emotion] = count
    
    if max(scores.values()) > 0:
        top_emotion = max(scores, key=scores.get)
    else:
        top_emotion = "neutral"
    
    return top_emotion, scores

def analyze_text(text):
    if not isinstance(text, str) or text == "" or pd.isna(text):
        return {'sentiment': 'SKIPPED', 'compound_score': 0, 'top_emotion': 'empty'}
    
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = "POSITIVE"
    elif compound <= -0.05:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"
    
    top_emotion, emotion_scores = detect_emotions(text)
    
    return {
        'sentiment': sentiment,
        'compound_score': compound,
        'top_emotion': top_emotion
    }

# LOAD THE LARGE CSV FILE
print("=" * 60)
print("LOADING AMAZON REVIEWS DATA...")
print("=" * 60)

# Use the large file
df = pd.read_csv('amazon_reviews_large.csv')

print(f"Loaded {len(df)} reviews")
print(f"Columns found: {list(df.columns)}")
print()

# Analyze each review
results = []
print("ANALYZING REVIEWS...")
print("-" * 60)

for index, row in df.iterrows():
    review_text = row['reviewText']
    product = row['productName']
    rating = row['rating']
    
    analysis = analyze_text(review_text)
    
    if analysis['sentiment'] != 'SKIPPED':
        results.append(analysis)
        # Print first 20 reviews as samples
        if index < 20:
            print(f"{index+1}. [{product}] \"{review_text[:50]}...\"")
            print(f"   → Sentiment: {analysis['sentiment']} | Emotion: {analysis['top_emotion'].upper()}")
    
    # Show progress every 10 reviews
    if (index + 1) % 10 == 0:
        print(f"   ... Processed {index+1}/{len(df)} reviews")

print()
print("=" * 60)
print("📊 FINAL ANALYSIS REPORT")
print("=" * 60)

# Sentiment Distribution
sentiment_counts = pd.Series([r['sentiment'] for r in results]).value_counts()
print("\n📈 SENTIMENT DISTRIBUTION:")
for sentiment, count in sentiment_counts.items():
    percentage = (count / len(results)) * 100
    bar = "█" * int(percentage / 2)
    print(f"   {sentiment}: {count:3d} reviews ({percentage:5.1f}%) {bar}")

# Emotion Distribution
emotion_counts = pd.Series([r['top_emotion'] for r in results]).value_counts()
print("\n😊 EMOTION DISTRIBUTION:")
for emotion, count in emotion_counts.items():
    percentage = (count / len(results)) * 100
    bar = "█" * int(percentage / 2)
    print(f"   {emotion.upper()}: {count:3d} reviews ({percentage:5.1f}%) {bar}")

# Summary
print("\n" + "-" * 40)
print("💡 KEY INSIGHTS:")
print("-" * 40)

pos_count = sentiment_counts.get('POSITIVE', 0)
neg_count = sentiment_counts.get('NEGATIVE', 0)
neu_count = sentiment_counts.get('NEUTRAL', 0)

if pos_count > neg_count:
    print(f"✅ Overall: Customers are POSITIVE ({pos_count/len(results)*100:.0f}% positive)")
else:
    print(f"❌ Overall: Customers are NEGATIVE ({neg_count/len(results)*100:.0f}% negative)")

top_emotion = emotion_counts.index[0] if len(emotion_counts) > 0 else "N/A"
print(f"🎭 Most common emotion: {top_emotion.upper()}")

print(f"\n📌 Total reviews analyzed: {len(results)}")
print("=" * 60)
print("✅ ANALYSIS COMPLETE!")
print("=" * 60)