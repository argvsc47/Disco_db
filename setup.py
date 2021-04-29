from distutils.core import setup

setup(
  name = 'DiscoDB',         # How you named your package folder (MyLib)
  packages = ['DiscoDB'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',     
  description = 'Disco is minimalist password encoded database system made in python, that emphasizes simplicity and efficiency',   # Give a short description about your library
  author = 'argvsc47',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/argvsc47/DiscoDB',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/argvsc47/DiscoDB/archive/v_10.tar.gz',    # I explain this later on
  keywords = ['Disco', 'Database', 'light', 'secure'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cryptography',
          'base64',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Database',
    'License :: OSI Approved :: GNU Public License 3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
