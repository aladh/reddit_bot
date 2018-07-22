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
                            f'sellsword. '
        ]
