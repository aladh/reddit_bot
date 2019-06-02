class LambdaQuotes:
    @staticmethod
    def all():
        return [
            lambda comment: f'u/{comment.author.name}, the next time Ser Meryn speaks, kill him.',
            lambda comment: f"I'm not questioning your honour, u/{comment.author.name}...I'm denying its existence!",
            lambda comment: f'Anyone named u/{comment.author.name} must be a pervert.',
            lambda comment: f"What do you want from me, u/{comment.author.name}? Gold? Women? Golden women? Stick "
                            f"with me and you'll have them all, for as long as I'm around and not a moment longer.",
            lambda comment: f'u/{comment.author.name}... I wish to confess. I wish to confess.',
            lambda comment: f"I WILL NOT GIVE MY LIFE FOR u/{comment.author.name}'S MURDER, AND I KNOW I'LL GET NO "
                            f"JUSTICE HERE!! SO I WILL LET THE GODS DECIDE MY FATE! I DEMAND A TRIAL BY COMBAT!!!",
            lambda comment: f'Let me give you some advice, u/{comment.author.name}: never forget what you are. The '
                            f'rest of the world will not. Wear it like armor, and it can never be used to hurt you.',
            lambda comment: f'Oh! "{sorted(comment.body.split(), key=len, reverse=True)[0]}". Fancy word for a '
                            f'sellsword.',
            lambda comment: f"Cut off u/{comment.author.name}'s manhood and feed it to the goats!",
            lambda comment: f'Get u/{comment.author.name} out of my sight! Throw them in one of the black cells!',
            lambda comment: f"It's hard to argue with u/{comment.author.name}'s assessment.",
            lambda comment: f"You have to admire u/{comment.author.name}'s imagination.",
            lambda comment: f"You have to admire u/{comment.author.name}'s imagination.",
            lambda comment: f"I was the smartest person I knew, certainly I had the wherewithal to unravel the "
                            f"mysteries that lay at the heart of u/{comment.author.name}.",
            lambda comment: f'You once said that without me, the city would have faced certain defeat. You said the '
                            f'histories would never mention me, but you would not forget. Have you forgotten, '
                            f'u/{comment.author.name}?',
            lambda comment: f"You may not believe it, but I've missed you, u/{comment.author.name}. Nobody glowers "
                            f"quite like you. "
        ]
