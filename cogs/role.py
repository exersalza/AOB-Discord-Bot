import json
from datetime import datetime
from itertools import cycle

import discord
from discord.ext import commands, tasks

from sql.sql_conn import cur, mydb
from etc.error_handler import invalid_argument


#todo:
# Permission check

class Roler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        cur.execute('SELECT * FROM discord_db')
        self.foo = []

        for i in cur.fetchall():
            self.foo.append(i[1])

        self.status = cycle(self.foo)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'\u001b[32m[STATUS]\u001b[0m ready bitch! {datetime.now().strftime("%H:%M:%S")}')

        await self.status_task.start()

    @tasks.loop(seconds=30)
    async def status_task(self):
        await self.bot.change_presence(status=discord.Status.idle,
                                       activity=discord.Activity(type=discord.ActivityType.playing,
                                                                 name=next(self.status)))

    @commands.command(aliases=['h'])
    async def help(self, ctx):
        """
        :param ctx:
        :return:

        Help Command
        """
        embed = discord.Embed(title='Help Site', description='<> Ist ein Pflicht feld', color=0xCD5D7D)
        embed.add_field(name=f'!add_cycle <arg> or !adc', value='Fügt ein Objekt für die ActivityBar hinzu!', inline=False)
        embed.add_field(name=f'!show_cycle or !shc', value='Zeigt dir die Objekte in der ActivityBar an!', inline=False)
        embed.add_field(name=f'!rm_cycle <id> or !rmc', value='Löscht ein Objekt aus der ActivityBar', inline=False)
        embed.add_field(name=f'\u200b', value='\u200b', inline=False)
        embed.add_field(name=f'!noice', value='Zeigt dir die anzahl an wie oft exersalza Noice geschrieben hat!', inline=False)
        embed.add_field(name=f'!roler', value='Ist selbsterklärend', inline=False)

        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['adc'])
    async def add_cycle(self, ctx, *, arg):
        """
        :param ctx:
        :param arg:
        :return:

        ActivityBar Cycle function -> !add_cycle / !adc
        """
        try:
            cur.execute(f"INSERT INTO discord_db (scroll_txt) VALUE ('{str(arg)}')")
            mydb.commit()

            self.foo.append(arg)

            await ctx.channel.send(f'Die ActivityBar hat sich geupdated!. `{arg}` ist nun in der Auswahl!')
        except Exception:   # Exception for SQL Errors
            await ctx.channel.send(f'Die Aktion hat leider nicht geklappt :)')
            pass

    @commands.command(aliases=['shc'])
    async def show_cycle(self, ctx):
        """
        :param ctx:
        :return:

        ActivityBar CMS -> !show_cycle / !shc
        """
        cur.execute('SELECT * FROM discord_db')

        await ctx.channel.send(cur.fetchall())

    @commands.command(aliases=['rmc'])
    async def rm_cycle(self, ctx, arg=''):
        """
        :param ctx:
        :param arg:
        :return:

        ActivityBar CMS -> !rm_cycle / !rmc
        """
        if arg == '':
            await invalid_argument(self, ctx, "rm_cycle")
            return
        elif not arg.isdigit():
            if not ',' in arg:
                await invalid_argument(self, ctx, "rm_cycle")
            return
        try:
            # cur.execute(f"DELETE FROM discord_db WHERE id = '{arg}'")
            # mydb.commit()

            cur.execute(f"SELECT * FROM discord_db WHERE id = '{arg}'")

            await ctx.channel.send(f'Die ActivityBar hat sich geupdated!. `{arg}` wurde gelöscht!')
        except Exception:
            await ctx.channel.send(f'Die Aktion hat leider nicht geklappt :)')
            pass

    @commands.command()
    async def roler(self, ctx):
        """
        :param ctx:
        :return:

        Just an fun command
        """
        await ctx.send(f'{ctx.message.author.mention} Just got an Roler Submariner')

    @commands.command()
    async def noice(self, ctx):
        """
        :param ctx:
        :return:

        Another fun command
        """
        with open('noice.json', 'r', encoding='utf-8') as f:
            noice = json.load(f)

        await ctx.channel.send(f'Es wurden schon: {noice["noice"]}x Noice auf den Server geschrieben!')

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        :param message:
        :return:

        Message Control area -> Noice, whoami command
        """

        if message.author.bot:
            return

        if not '!' in message.content and 'noice' in str(message.content).lower():
            with open('noice.json', 'r', encoding='utf-8') as f:
                noice = json.load(f)

            noice['noice'] += 1

            await message.channel.send(f'Es wurden bereits {noice["noice"]}x ein Noice geschrieben!')

            with open('noice.json', 'w', encoding='utf-8') as f:
                json.dump(noice, f)

        if 'whoami' in message.content:
            await message.channel.send(message.author.mention)


def setup(bot):
    bot.add_cog(Roler(bot))
