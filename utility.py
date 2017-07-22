from collections import OrderedDict

from discord.ext import commands


class Utility:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx: commands.Context, question: commands.clean_content, *options: commands.clean_content):
        """
        Start a vote given a question and 2-9 options.
        Surround the question and options with " if they're more than one word.
        """
        if len(options) < 2:
            raise commands.BadArgument("At least two options are required to create a vote.")
        if len(options) > 9:
            raise commands.BadArgument("A vote can have a maximum of 9 options.")

        options_dict = OrderedDict((keycap(i), opt) for i, opt in enumerate(options, 1))
        options_str = '\n'.join(f'{kc} - {opt}' for kc, opt in options_dict.items())
        vote = await ctx.send(f"{ctx.author.display_name}: {question}\n\n{options_str}")
        for kc in options_dict.keys():
            await vote.add_reaction(kc)


def keycap(i: int) -> str:
    return f"{chr(0x30+i)}{chr(0x20E3)}"


def setup(bot: commands.Bot):
    cog = Utility(bot)
    bot.add_cog(cog)
