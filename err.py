import time

from telegram.error import (BadRequest, ChatMigrated, NetworkError,
                            TelegramError, TimedOut, Unauthorized)


def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        # remove update.message.chat_id from conversation list
        print(time.asctime( time.localtime(time.time()) ), ':', 'Unathorized')
    except BadRequest:
        # handle malformed requests - read more below!
        print(time.asctime( time.localtime(time.time()) ), ':', 'Bad Request error')
    except TimedOut:
        # handle slow connection problems
        print(time.asctime( time.localtime(time.time()) ), ':', 'Timed out')
    except NetworkError:
        # handle other connection problems
        print(time.asctime( time.localtime(time.time()) ), ':', 'Network error')
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print(print(time.asctime( time.localtime(time.time()) ), ':', 'Bad Request error'))
    except TelegramError:
        print(time.asctime( time.localtime(time.time()) ), ':', 'Telegram error')
        # handle all other telegram related errors
