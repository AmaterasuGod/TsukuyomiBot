import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog online.')

    #Commands
    @commands.command()
    async def dadjoke(self, ctx):
        responses = ['What do you call a mac ‘n’ cheese that gets all up in your face? Too close for comfort food!',
                    'What concert costs just 45 cents? 50 Cent featuring Nickelback!',
                    'Why did the scarecrow win an award? Because he was outstanding in his field!',
                    'What do sprinters eat before a race? Nothing, they fast!',
                    'Why couldn’t the bicycle stand up by itself? It was two tired!',
                    'Did you hear about the restaurant on the moon? Great food, no atmosphere!',
                    'What do you call a fish with two knees? A two-knee fish!',
                    'Why do melons have weddings? Because they cantaloupe!',
                    'What happens when you go to the bathroom in France? European.',
                    "What’s the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle? Attire!",
                    'How many apples grow on a tree? All of them!',
                    'Did you hear the rumor about butter? Well, I’m not going to spread it!',
                    "Did you hear about the guy who invented Lifesavers?  They say he made a mint!",
                    "Why do you never see elephants hiding in trees? Because they’re so good at it!",
                    "How does a penguin build its house? Igloos it together!",
                    'Why did the old man fall in the well? Because he couldn’t see that well!',
                    "Why don’t skeletons ever go trick or treating? Because they have no body to go with!",
                    'What do you call a factory that sells passable products? A satisfactory!',
                    "Why did the invisible man turn down the job offer? He couldn’t see himself doing it!",
                    "Want to hear a joke about construction? I’m still working on it!"
                    'I like telling Dad jokes. Sometimes he laughs!',
                    'To whoever stole my copy of Microsoft Office, I will find you. You have my Word!',
                    'I used to work in a shoe-recycling shop. It was sole destroying!',
                    'My boss told me to have a good day. So I went home!',
                    "I’m so good at sleeping I can do it with my eyes closed!",
                    'Spring is here! I got so excited I wet my plants!',
                    "I thought about going on an all-almond diet… But that’s just nuts!",
                    'This graveyard looks overcrowded. People must be dying to get in there!',
                    "My friend says to me, “What rhymes with orange?”And I told him, “No it doesn’t!”",
                    'My wife told me I had to stop acting like a flamingo. So I had to put my foot down!',
                    'I told my girlfriend she drew her eyebrows too high. She seemed surprised!',
                    'I tell dad jokes but I have no kids…I’m a faux pa!',
                    "So a vowel saves another vowel’s life. The other vowel says, “Aye E! I owe you!”",
                    'Did I tell you the time I fell in love during a backflip? I was heels over head!',
                    "My uncle named his dogs Rolex and Timex. They’re his watch dogs!",
                    'If you see a robbery at an Apple Store does that make you an iWitness?!',
                    "I would avoid the sushi if I was you. It’s a little fishy!",
                    "Five out of four people admit they’re bad with fractions!",
                    'Two goldfish are in a tank. One says to the other, “Do you know how to drive this thing?”',
                    "I’ll call you later. Don’t call me later, call me Dad!",
                    'Did you hear about the Italian chef who died? He pasta way!',
                    "When the grocery store clerk asks me if I want the milk in a bag, I always tell him, “No, I’d rather drink it out of the carton!”",
                    'The difference between a numerator and a denominator is a short line. Only a fraction of people will understand this!',
                    "What’s ET short for? Because he’s only got tiny legs!",
                    "I don’t play soccer because I enjoy the sport. I’m just doing it for kicks!",
                    'What’s brown and sticky? A stick!',
                    'Can February March? No, but April May!',
                    "What’s orange and sounds like a parrot? A carrot!",
                    'I invented a new word today: Plagiarism!',
                    'What do you call a donkey with only three legs? A wonkey!',
                    'After dinner, my wife asked if I could clear the table. I needed a running start, but I made it!',
                    'How do you make a Kleenex dance? Put some boogie in it!',
                    'Why is Peter Pan always flying? He neverlands!',
                    "What’s a ninja’s favorite type of shoes? Sneakers!",
                    "This morning, Siri said, “Don’t call me Shirley.” I accidentally left my phone in Airplane mode!",
                    "A woman is on trial for beating her husband to death with his guitar collection. The judge asks her, “First offender?” She says, “No, first a Gibson! Then a Fender!”",
                    'I know a lot of jokes about retired people but none of them work!',
                    'What do you call a guy with a rubber toe? Roberto!',
                    "What do Santa’s elves listen to ask they work? Wrap music!",
                    'What rhymes with boo and stinks? You!',
                    "If an English teacher is convicted of a crime and doesn’t complete the sentence, is that a fragment?",
                    "I think my wife is putting glue on my antique weapons collection. She denies it but I’m sticking to my guns!",
                    'Which U.S. state is famous for its extra-small soft drinks? Minnesota!',
                    "I got a hen to regularly count her own eggs. She’s a real mathamachicken!",
                    "What did the Ranch say when someone opened the refrigerator door? “Close the door, I’m dressing!”",
                    'Why do trees seem suspicious on sunny days? They just seem a little shady!',
                    "What did the policeman say to his belly button? You’re under a vest!",
                    'Last night I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.',
                    'A cheese factory exploded in France. Da brie is everywhere!',
                    'What do you call a fake noodle? An Impasta!',
                    "I’ve been bored recently so I’ve decided to take up fencing. The neighbors said they will call the police unless I put it back.",
                    'Why did the math book look so sad? Because of all of its problems!',
                    "I don’t really call for funerals that start before noon. I guess I’m just not a mourning person!",
                    'If two vegans get in a fight, is it still considered a beef?',
                    'One of my favorite memories as a kid was when my brothers used to put me inside a tire and roll me down a hill. They were Goodyears!']
        await ctx.send(f' {random.choice(responses)}')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
            responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def add(self, ctx, a: int, b: int):
            await ctx.send(a+b)
    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(a*b)
    @commands.command()
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there!")
    @commands.command()
    async def cat(self, ctx):
            responses = ['https://media2.giphy.com/media/H4DjXQXamtTiIuCcRU/giphy.webp?cid=790b7611ecc9d87a72a271d52ff9389d339e03769469c5e8&rid=giphy.webp',
                    'https://media1.giphy.com/media/1ViLp0GBYhTcA/giphy.webp?cid=790b7611ecc9d87a72a271d52ff9389d339e03769469c5e8&rid=giphy.webp',
                    'https://media3.giphy.com/media/6VoDJzfRjJNbG/200.webp?cid=790b76116b7907eab875596d11aece7dc4e1b7d14fbdef84&rid=200.webp',
                    'https://media0.giphy.com/media/11c7UUfN4eoHF6/giphy.webp?cid=790b76116b7907eab875596d11aece7dc4e1b7d14fbdef84&rid=giphy.webp',
                    'https://media1.giphy.com/media/b5XJRNBrvgVHjkTsRV/giphy.webp?cid=790b76116b7907eab875596d11aece7dc4e1b7d14fbdef84&rid=giphy.webp',
                    'https://media1.giphy.com/media/JIX9t2j0ZTN9S/giphy.webp?cid=790b7611014596463846fa9c1d40cd57138def0bca8e5cf6&rid=giphy.webp',
                    'https://media0.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.webp?cid=790b7611014596463846fa9c1d40cd57138def0bca8e5cf6&rid=giphy.webp',
                    'https://media0.giphy.com/media/WYEWpk4lRPDq0/giphy.webp?cid=790b7611014596463846fa9c1d40cd57138def0bca8e5cf6&rid=giphy.webp',
                    'https://media0.giphy.com/media/Jjo6WPW26zDdS/200.webp?cid=790b7611014596463846fa9c1d40cd57138def0bca8e5cf6&rid=200.webp'
                    'https://media0.giphy.com/media/9Vvoj75o3ZsK6TRUqH/giphy.webp?cid=790b7611014596463846fa9c1d40cd57138def0bca8e5cf6&rid=giphy.webp',
                    'https://media0.giphy.com/media/pkzecz3ucmVaw/200.webp?cid=790b76116b7907eab875596d11aece7dc4e1b7d14fbdef84&rid=200.webp',
                    'https://media1.giphy.com/media/f9Shx16Et4iSVQFKR1/giphy.webp?cid=790b7611181b2f0c594816fc5fca127d59b6b9a89723eeb4&rid=giphy.webp']
            await ctx.send(f' {random.choice(responses)}')

    @commands.command()
    async def hug(self, ctx, member : discord.Member):
            responses = ['https://media.giphy.com/media/wnsgren9NtITS/giphy.gif',
                    'https://media.giphy.com/media/143v0Z4767T15e/giphy.gif',
                    'https://media.giphy.com/media/cotftb3AXgfV6/giphy.gif',
                    'https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif',]
def setup(bot):
    bot.add_cog(Fun(bot))
