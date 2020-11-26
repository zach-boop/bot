import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = open("./token.txt", "r").read()


#loot tracker
@client.group()
async def loot(ctx):
    loot = open("./loot.txt", "r")
    if ctx.invoked_subcommand is None:
        await ctx.send(loot.read())
    loot.close()


@loot.command()
async def addLoot(ctx, arg):
  	loot = open("./loot.txt", "a+")
  	loot.write(f"\n{arg}")
  	loot.close()
  	loot = open("./loot.txt", "r")
  	await ctx.send(loot.read())
  	loot.close()


#set bot status to playing dnd
@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('Dungeons and Dragons'))


#load commands
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send('loaded cog')


@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send('reloaded cog')


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send('unloaded cog')


#spells
@client.command(aliases=["spell"])
async def spells(ctx):
	await ctx.send(
	    '```For more help enter:\n  .spellsCleric\n    .spellsDruid\n  .spellsMagicUser\n    .spellsIllusionist```'
	)


#close
@client.command(aliases=['close', 'die', 'exit'])
@commands.is_owner()
async def shutdown(ctx):
	await ctx.bot.logout()
	print("Bot Closed")


#help command
client.remove_command('help')


@client.group(aliases = ["Help"])
async def help(ctx):
    if ctx.invoked_subcommand is None:
        helpcom = discord.Embed(
            colour=discord.Colour(0xdeb887),
            title="Help:",
            description="Will get around to adding a description here."
        )
        helpcom.add_field(name = "Race", value = ".Help Race")
        helpcom.add_field(name = "Class", value = ".Help Class")
        helpcom.add_field(name = "Alignment", value = ".Help Alignment")
        helpcom.add_field(name = "Spells", value = ".Help Spells")
        helpcom.add_field(name = "Misc", value = ".Help Misc")
        await ctx.send(embed=helpcom)

@help.command(aliases = ["Race"])
async def race(ctx):
    race = discord.Embed(
        colour=discord.Colour(0xdeb887),
        title="Race:", 
        description= "will add one later"
    )
    race.add_field(name = "Dwarf:", value = ".dwarf shows info of Dwarf")
    race.add_field(name = "Elf:", value = ".elf shows info of Elf")
    race.add_field(name = "Gnome:", value = ".gnome shows info of Gnome")
    race.add_field(name = "Half-Elf:", value = ".halfelf shows info of Half-Elf")
    race.add_field(name = "Halfling:", value = ".halfling shows info of Halfling")
    race.add_field(name = "Half-Orc:", value = ".halforc shows info of Half-Orc")
    race.add_field(name = "Human:", value = ".human shows info of Human")
    await ctx.send(embed=race)

@help.command(aliases = ["class"])
async def Class(ctx):
    clas = discord.Embed(
        colour=discord.Colour(0xdeb887),
        title="Class:", 
        description= "will add one later"
    )
    clas.add_field(name = "Cleric:", value = "cleric shows info of Cleric")
    clas.add_field(name = "Druid:", value = ".druid shows info of Druid")
    clas.add_field(name = "Fighter:", value = ".fighter shows info of Fighter")
    clas.add_field(name = "Ranger:", value = ".ranger shows info of Ranger")
    clas.add_field(name = "Barbarian:", value = ".barbarian shows info of Barbarian")
    clas.add_field(name = "Cavalier:", value = ".cavalier shows info of Cavalier")
    clas.add_field(name = "Paladin:", value = ".paladin shows info of Paladin")
    clas.add_field(name = "Magic-User:", value = ".magicuser shows info of Magic-User")
    clas.add_field(name = "Illusionist:", value = ".illusionist shows info of Illusionist")
    clas.add_field(name = "Theif:", value = ".theif shows info of Theif")
    clas.add_field(name = "Assassin:", value = ".assassin shows info of Assassin")
    clas.add_field(name = "Monk", value = ".monk shows info of Monk")
    clas.add_field(name = "Bard", value = ".bard shows info of Bard")
    clas.add_field(name = "Scout", value = ".scout shows info of Scout")
    clas.add_field(name = "Delver", value = ".delver shows info of Delver")
    await ctx.send(embed=clas)

@help.command(aliases = ["alignment"])
async def Alignment(ctx):
    align = discord.Embed(
        coulor = discord.Colour(0xdeb887),
        title = "Alignment",
        description = "Naturally, there are all variations and shades of tendencies within each alignment. The descriptions are generalizations only. A character can be basically good in its 'true' neutrality, or tend towards evil. It is probable that your campaign referee will keep a graph of the drift of your character on the alignment chart. This is affected by the actions (and desires) of your character during the course of each adventure, and will be reflected on the graph. You may find that these actions are such as to cause the declared alignment to be shifted towards, or actually to, some other."
    )
    align.add_field(name = "Lawful Good", value = "While as strict in their prosecution of law and order, characters of lawful good alignment follow these precepts to improve the common weal. Certain freedoms must, of course, be sacrificed in order to bring order; but truth is of highest value, and life and beauty of great importance. The benefits of this society are to be brought to all.")
    align.add_field(name = "Lawful Neutral", value = "Those of this alignment view regulation as all-important, taking a middle road betwixt evil and good. This is because the ultimate harmony of the world -and the whole of the universe - is considered by lawful neutral creatures to have its sole hope rest upon law and order. Evil or good are immaterial beside the determined purpose of bringing all to predictability and regulation.")
    align.add_field(name = "Lawful Evil", value = "Creatures of this alignment are great respecters of laws and strict order, but life, beauty, truth, freedom and the like are held as valueless, or at least scorned. By adhering to stringent discipline, those of lawful evil alignment hope to impose their yoke upon the world.")
    align.add_field(name = "Neutral Good", value = "Unlike those directly opposite them (neutral evil) in alignment, creatures of neutral good believe that there must be some regulation in combination with freedoms if the best is to be brought to the world - the most beneficial conditions for living things in general and intelligent creatures in particular.")
    align.add_field(name = "True Neutral", value = "The 'true' neutral looks upon all other alignments as facets of the system of things. Thus, each aspect - evil and good, chaos and law - of things must be retained in balance to maintain the status quo; for things as they are cannot be improved upon except temporarily, and even then but superficially. Nature will prevail and keep things as they were meant to be, provided the 'wheel' surrounding the hub of nature does not become unbalanced due to the work of unnatural forces - such as human and other intelligent creatures interfering with what is meant to be.")
    align.add_field(name = "Neutral Evil", value = "The neutral evil creature views law and chaos as unnecessary considerations, for pure evil is all-in-all. Either might be used, but both are disdained as foolish clutter useless in eventually bringing maximum evilness to the world.")
    align.add_field(name = "Chaotic Good", value = "While creatures of this alignment view freedom and the randomness of action as ultimate truths, they likewise place value on life and the welfare of each individual. Respect for individualism is also great. By promoting the gods of chaotic good, characters of this alignment seek to spread their values throughout the world.")
    align.add_field(name = "Chaotic Neutral", value = "Above respect for life and good, or disregard for life and promotion of evil, the chaotic neutral places randomness and disorder. Good and evil are complimentary balance arms. Neither are preferred, nor must either prevail, for ultimate chaos would then suffer.")
    align.add_field(name = "Chaotic Evil", value = "The major precepts of this alignment are freedom, randomness, and woe. Laws and order, kindness, and good deeds are disdained. life has no value. By promoting chaos and evil, those of this alignment hope to bring themselves to positions of power, glory, and prestige in a system ruled by individual caprice and their own whims.")
    await ctx.send(embed=align)

@help.command(aliases = ["spell", "Spells", "spells"])
async def Spell(ctx):
    spell = discord.Embed(
        coulor = discord.Colour(0xdeb887),
        title = "Spell",
        description = "will add later"
    )
    spell.add_field(name = "To find info about a certain spell enter", value = ".spell(spellname)")
    spell.add_field(name = "To find out about what spells Clerics can cast:", value = ".spellsCleric")
    spell.add_field(name = "To find out about what spells Druids can cast:", value = ".spellsDruid")
    spell.add_field(name = "To find out about what spells Magic-User can cast:", value = ".spellsMagicUser")
    spell.add_field(name = "To find out about what spells Illusionist can cast:", value = ".spellsIllusionist")
    await ctx.send(embed=spell)

@help.command(aliases = ["misc"])
async def Misc(ctx):
    misc = discord.Embed(
        coulor = discord.Colour(0xdeb887),
        title = "Misc",
        description = "Random commands..."
    )
    misc.add_field(name = "Market:", value = ".market")
    misc.add_field(name = "Rule Books:", value = ".rulebook")
    await ctx.send(embed=misc)

@client.command(aliases = ["invite"])
async def link(ctx):
    await ctx.send("Invite link\nhttps://discord.gg/yR8H92qM4d")

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
