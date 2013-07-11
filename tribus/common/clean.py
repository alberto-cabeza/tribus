import os
from distutils.cmd import Command
from distutils.command.clean import clean as base_clean

from tribus.config.base import BASEDIR, DOCDIR
from tribus.common.utils import get_path, find_files, find_dirs
from tribus.common.logger import get_logger

log = get_logger()


class clean_img(Command):
    description = 'Remove compiled PNG files from source.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for png_file in find_files(path=BASEDIR, pattern='*.png'):
            if os.path.isfile(png_file):
                try:
                    os.remove(png_file)
                    log.debug("[%s.%s] Removing \"%s\"." % (__name__,
                                                            self.__class__.__name__,
                                                            png_file))
                except Exception, e:
                    print e


class clean_html(Command):
    description = 'Compile .po files into .mo files'
    user_options = []

    def initialize_options(self):
        pass
 
    def finalize_options(self):
        pass
 
    def run(self):
        for html_file in find_files(path=get_path([DOCDIR, 'html']), pattern='*.*'):
            if os.path.isfile(html_file):
                try:
                    os.remove(html_file)
                    log.debug("[%s.%s] Removing \"%s\"." % (__name__, self.__class__.__name__, html_file))
                except Exception, e:
                    print e

        for html_dir in reversed(find_dirs(path=get_path([DOCDIR, 'html']))):
            try:
                os.rmdir(html_dir)
                log.debug("[%s.%s] Removing \"%s\"." % (__name__, self.__class__.__name__, html_dir))
            except Exception, e:
                print e


class clean_man(Command):
    description = 'Compile .po files into .mo files'
    user_options = []

    def initialize_options(self):
        pass
 
    def finalize_options(self):
        pass
 
    def run(self):
        man_file = get_path([DOCDIR, 'man', 'tribus.1'])
        if os.path.isfile(man_file):
            try:
                os.remove(man_file)
                log.debug("[%s.%s] Removing \"%s\"." % (__name__, self.__class__.__name__, man_file))
            except Exception, e:
                print e


class clean_mo(Command):
    description = 'Compile .po files into .mo files'
    user_options = []

    def initialize_options(self):
        pass
 
    def finalize_options(self):
        pass
 
    def run(self):
        for mo_file in find_files(path=BASEDIR, pattern='*.mo'):
            if os.path.isfile(mo_file):
                try:
                    os.remove(mo_file)
                    log.debug("[%s.%s] Removing \"%s\"." % (__name__, self.__class__.__name__, mo_file))
                except Exception, e:
                    print e

class clean(base_clean):
    def run(self):
        self.run_command('clean_mo')
        self.run_command('clean_img')
        self.run_command('clean_html')
        self.run_command('clean_man')
        base_clean.run(self)

