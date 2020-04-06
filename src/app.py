class App:
    def __init__(self, name, version = '0.1.a', desc = 'yet Another Sit'):
        self.__name = name
        self.__version = version
        self.__desc = desc
        self.__funcList = {}
        self.__authors = {}

        self.__flags = []
        self.__subargs = []

    def addAuthor(self, name, email = 'MISSING', about = ''):
        self.__authors[name] = {'email': email, 'about': about}


    def args(self, arg, usage, desc, **kwargs):
        def inner(func):
            self.__funcList[arg] = {
                'func': func,
                'usage': usage,
                'desc': desc,
            }
            if 'must_count' in kwargs:
                self.__funcList[arg]['must_count'] = kwargs['must_count']

            return func

        return inner

    def __printAuthors(self):
        for i in self.__authors:
            print('%s <%s> %s' %(i,self.__authors[i]['email'], self.__authors[i]['about']))

    def PrintHelp(self, spec_func = None):
        if spec_func is None:
            print('{} {}'.format(self.__name, self.__version))
            print(self.__desc)
            self.__printAuthors()
            print('Usage:')
            for i in self.__funcList:
                f = self.__funcList[i]
                print('\t{} {} :\t\t {}'.format(i, f['usage'], f['desc']))

    def run(self, args):
        func = None
        for i in args:
            if i in self.__funcList:
                func = self.__funcList[i]
            else:
                if i[0:2] == '--':
                    self.__flags.append(i[2:])
                elif i[0:1] == '-':
                    self.__flags.append(i[1:])
                else:
                    self.__subargs.append(i)

        if func is None:
            if 'main' in self.__funcList:
                self.__funcList['main']['func'](self._in_built(self.__subargs, self.__flags, args))
            else:
                self.PrintHelp()
        else:
            if 'must_count' in func and func['must_count'] != len(self.__subargs):
                print('Must have %d arguments but %d provided' % (func['must_count'], len(self.__subargs)))
            else:
                func['func'](self._in_built(self.__subargs, self.__flags, args))

    class _in_built:
        def __init__(self,args, flags,all_args):
            self.__args = args
            self.__flags = flags
            self.__all_args = all_args

        def is_set(self, flag):
            if flag in self.__flags:
                return True
            else:
                return False

        def value_of(self, arg, default_value = None):
            for i in self.__flags:
                if '=' in i:
                    if i[0:i.index('=')] == arg:
                        return i[i.index('=') + 1:]
            return default_value

        def get_args(self):
            return self.__args[1:]
