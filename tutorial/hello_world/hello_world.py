
import inkex

class hello_world(inkex.EffectExtension):

    def effect(self):
        self.msg("Hello world!")
		
if __name__ == '__main__':
    hello_world().run()
