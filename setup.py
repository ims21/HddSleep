from distutils.core import setup
import setup_translate

pkg = 'Extensions.HddSleep'
setup (name = 'enigma2-plugin-extensions-hddsleep',
       version = '1.70',
       description = 'plugin for hdd sleep',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['locale/*.pot', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
