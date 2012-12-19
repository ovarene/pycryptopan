from distutils.core import setup
f=open("README.rst")
setup(name='pycryptopan', version='0.01',
            py_modules=['cryptopan'],
            requires=['pycrypto'],
            url="https://github.com/FFM/pycryptopan",
            author="Michael Bauer",
            email="mihi@lo-res.org",
            description="""A python implementation of Crypto-PAn 
              a ip anonymization algorithm""",
            long_description="\n".join(f)
                  )
