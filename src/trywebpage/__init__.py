from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    main_article = {
        'title': 'Miracle Recovery: Guinea Pig Ollie Bounces Back from Weight Loss',
        'subtitle': 'Local pet\'s inspiring journey to health captures hearts',
        'author': 'Sarah Johnson',
        'date': datetime.now().strftime('%B %d, %Y'),
        'category': 'PETS & LIFESTYLE',
        'featured': True,
        'content': """
        In a heartwarming turn of events, Ollie, a beloved guinea pig from the local community, 
        has shown remarkable progress in her recovery after losing nearly half her body weight. 
        The small but resilient rodent has become an inspiration to pet owners and veterinarians alike.

        "We were extremely concerned when Ollie's weight dropped so dramatically," says Dr. Maria 
        Rodriguez, the veterinarian overseeing Ollie's care. "But her determination to recover 
        has been nothing short of extraordinary."

        Through a carefully monitored diet and supportive care, Ollie has steadily been regaining 
        her strength and mass. Her temporary owner, Katja Roose, reports that she's back to her 
        cheerful self, eagerly anticipating her daily vegetables and hay.

        "It's amazing to see her bounce back," Roose says, watching Ollie munch on a piece 
        of bell pepper. "She's already regained 30% of her lost weight, and her energy levels 
        are through the roof."
        """
    }
    
    other_articles = [
        {
            'title': 'Tech Giants Announce Revolutionary AI Breakthrough',
            'subtitle': 'New algorithm achieves human-like reasoning capabilities',
            'author': 'Michael Chen',
            'date': datetime.now().strftime('%B %d, %Y'),
            'category': 'TECHNOLOGY',
            'featured': False,
            'content': 'Leading tech companies unveiled a groundbreaking AI system today...'
        },
        {
            'title': 'Global Climate Summit Reaches Historic Agreement',
            'subtitle': 'Nations commit to ambitious carbon reduction targets',
            'author': 'Emma Roberts',
            'date': datetime.now().strftime('%B %d, %Y'),
            'category': 'CLIMATE',
            'featured': False,
            'content': 'In a landmark decision, world leaders have agreed to...'
        },
        {
            'title': 'Local Restaurant Wins Prestigious Culinary Award',
            'subtitle': 'Farm-to-table establishment recognized for innovation',
            'author': 'David Martinez',
            'date': datetime.now().strftime('%B %d, %Y'),
            'category': 'FOOD',
            'featured': False,
            'content': 'Downtown\'s favorite hidden gem has been awarded...'
        }
    ]
    
    opinions = [
        {
            'title': 'Why Guinea Pigs Are the Ultimate Teachers of Resilience',
            'author': 'Dr. Jennifer Hayes',
            'category': 'PERSPECTIVE'
        },
        {
            'title': 'The Hidden Cost of Pet Healthcare: We Need Reform Now',
            'author': 'Marcus Thompson',
            'category': 'OPINION'
        },
        {
            'title': 'Small Pets, Big Lessons: What Ollie Taught Us About Recovery',
            'author': 'Katja Roose',
            'category': 'OPINION'
        },
        {
            'title': 'Our Obsession with Pet Weight Loss Stories Must Stop',
            'author': 'Sandra Liu',
            'category': 'PERSPECTIVE'
        },
        {
            'title': 'The Real Reason Why Pet Obesity Is On The Rise',
            'author': 'Dr. Robert Chen',
            'category': 'ANALYSIS'
        }
    ]
    
    return render_template('index.html', main_article=main_article, other_articles=other_articles, opinions=opinions)

def main():
    app.run(debug=True)
