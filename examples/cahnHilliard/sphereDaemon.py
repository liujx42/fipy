import sys

from enthought.mayavi import mlab

from fipy.viewers.mayaviViewer.mayaviDaemon import MayaviDaemon

class SphereDaemon(MayaviDaemon):
    
    def view_data(self):
        """Sets up the mayavi pipeline for the visualization.
        """
        var = mlab.pipeline.set_active_attribute(self.cellsource, cell_scalars=r"$\phi$")
        
        clip = mlab.pipeline.data_set_clipper(var)

        clip.widget.widget_mode = 'Box'
        clip.widget.widget.place_factor = 1.
        clip.widget.widget.place_widget(0, 10, 0, 10, 0, 10)
        clip.widget.update_implicit_function()

        clip.widget.visible = False

        s = mlab.pipeline.surface(clip, vmin=self.datamin, vmax=self.datamax, colormap='hot')
        s.module_manager.scalar_lut_manager.show_scalar_bar = True

        
def main(argv=None):
    """Simple helper to start up the mayavi application.  This returns
    the running application."""
    m = SphereDaemon()
    m.main(argv)
    return m

if __name__ == '__main__':
    main(sys.argv[1:])
