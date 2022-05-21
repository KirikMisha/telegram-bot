from config import dp
from aiogram.utils import executor

from handlers import comands
from handlers import expanded_game
from handlers import expanded_vocabluary
from handlers import expanded_links
from handlers import expanded_grammar

comands.menu_hendlers(dp)
expanded_game.expanded_game_f(dp)
expanded_vocabluary.expanded_vocabulary_f(dp)
expanded_grammar.expanded_grammar_f(dp)
expanded_links.expanded_links_f(dp)


executor.start_polling(dp, skip_updates=True)
