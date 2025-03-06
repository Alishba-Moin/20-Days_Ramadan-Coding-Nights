from fastapi import FastAPI, Query, HTTPException
import random

app = FastAPI()

# Data Lists
side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

# Secure API Key
API_KEY = "1234567890"

# Health Check API
@app.get("/health")
def health_check():
    """Check if API is running"""
    return {"status": "API is running smoothly!"}


# Fetch Random Side Hustles
@app.get("/side_hustles")
def get_side_hustles(api_key: str, count: int = Query(1, ge=1, le=len(side_hustles))):
    """Returns a random side hustle idea"""
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {"side_hustles": random.sample(side_hustles, count)}


# Fetch Random Money Quotes
@app.get("/money_quotes")
def get_money_quotes(api_key: str, count: int = Query(1, ge=1, le=len(money_quotes))):
    """Returns a random money quote"""
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {"money_quotes": random.sample(money_quotes, count)}
