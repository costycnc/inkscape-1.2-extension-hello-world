
from inkex import (Boolean, Circle, EffectExtension, Layer, PathElement,
                   TextElement, errormsg, paths)
import datetime	,sys			   
				   

class hello(EffectExtension):

    def effect(self):  

        selected_nodes = self.options.selected_nodes	
			
        for item in selected_nodes:
            path_id, subpath_index, node_index = item.split(':')
            self.msg("node")
            self.msg(node_index)
			

					
if __name__ == '__main__':
    hello().run()
