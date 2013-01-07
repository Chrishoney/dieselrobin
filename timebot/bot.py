from collections import namedtuple
import ConfigParser
import datetime
import logging
import re
import os

from irc.bot import SingleServerIRCBot

DEBUG = True

logger = logging.getLogger(__name__)
if DEBUG:
    logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
if DEBUG:
    console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)

time_strings = {
    'before': 'dieselrobin starts in %s, %s hours, %s minutes, and %s seconds',
    'during': 'dieselrobin ends in %s, %s hours, %s minutes, and %s seconds',
    'after': 'dieselrobin is over',
}

def delta_to_string(delta, cond):

    def day_plural(days):
        return (str(days) + ' day') if days == 1 else (str(days) + ' days')

    def seconds_to_t(seconds):
        hour_div, min_div = 3600, 60
        hours, rem = divmod(seconds, hour_div)
        minutes, seconds = divmod(rem, min_div)
        return (hours, minutes, seconds)

    days = day_plural(delta.days)
    hours, minutes, seconds = seconds_to_t(delta.seconds)
    return time_strings[cond] % (days, hours, minutes, seconds)

class Timebot(SingleServerIRCBot):

    def __init__(self, channel, nick, server, port):
        super(Timebot, self).__init__([(server, port)], nick, nick)
        self.start_time = datetime.datetime(2013, 1, 4, 19, 00)
        self.end_time = datetime.datetime(2013, 1, 20, 19, 00)
        self.channel = channel
        self.server = server
        self.port = port
        self.nick = nick

    ################## 
    # Event Handlers #
    ################## 
    
    def on_welcome(self, c, e):
        ''' Join the channel specified in the config file. '''
        c.join(self.channel)
        logger.debug('Connected to %s' % self.channel)

    def on_pubmsg(self, c, e):
        ''' Execute the command if it is valid and respond to the channel. '''
        self.handle_command(c, e, e.arguments[0], e.target)
        logger.debug('Message sent to %s' % e.target)

    ################# 
    # User Commands #
    ################# 
    def handle_command(self, c, e, args, source):
        if args.startswith('!time'):
            self.time(c, e, args, source)
            
    def time(self, c, e, args, source):
        ''' !time. returns time left until the tournament is over '''
        now = datetime.datetime.now()
        start_delta = self.start_time - now
        end_delta = self.end_time - now
        if start_delta.days >= 0:
            msg = delta_to_string(start_delta, 'before')
        elif start_delta.days < 0 <= end_delta.days:
            msg = delta_to_string(end_delta, 'during')
        elif end_delta.days < 0:
            msg = time_strings['after']
        else:
            logger.warn('Unexpected case fall-through in time function')
        c.privmsg(source, msg)

#################
# Configuration #
#################

def parse_config(rc='~/.botrc'):
    ''' Parse the default config file and return a dict of settings '''
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser(rc))
    options = ['server', 'port', 'channel', 'nick']
    header = 'connection'
    settings = dict(zip(
        options,
        [config.get(header, option) for option in options]
    ))
    settings['port'] = int(settings['port'])
    return settings


################
# Main Program #
################
def main():
    settings = parse_config()
    server  = settings['server']
    port    = settings['port']
    nick    = settings['nick']
    channel = settings['channel']
    bot = Timebot(channel, nick, server, port)
    bot.start()

if __name__ == '__main__':
    main()
