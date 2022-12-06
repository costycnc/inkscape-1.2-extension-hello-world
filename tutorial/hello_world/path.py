
import inkex

class hello(inkex.EffectExtension):

    def effect(self):
        current_layer = self.svg.get_current_layer()
        path_list = current_layer.xpath('./svg:path')
        if len(path_list) < 1:
            inkex.errormsg('No path found !')
            return
        for path in path_list:
            path_id = path.get_id()
            csp = path.path.to_superpath()
            self.msg(csp)


		
if __name__ == '__main__':
    hello().run()
