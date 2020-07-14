from gi.repository import Gtk, Gdk
import gi
gi.require_version("Gtk", "3.0")


class DefaultCalendar(Gtk.Window):

    def __init__(self):
        super(DefaultCalendar, self).__init__()
        self.set_title("Calendar Demo")
        self.set_size_request(300, 200)
        # self.set_position(Gtk.WIN_POS_CENTER)

        vbox = Gtk.VBox(False, 5)
        self.cal = Gtk.Calendar()
        halign1 = Gtk.Alignment()
        halign1.add(self.cal)

        self.cal.set_display_options(0)
        # valign = Gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(halign1, True, True, 0)

        self.btn1 = Gtk.Button("set")
        self.btn2 = Gtk.Button("heading")
        self.btn3 = Gtk.Button("day name")
        self.btn4 = Gtk.Button("Both")

        hbox = Gtk.HBox(True, 3)
        hbox.add(self.btn1)
        hbox.add(self.btn2)
        hbox.add(self.btn3)
        hbox.add(self.btn4)

        halign = Gtk.Alignment()
        halign.add(hbox)

        vbox.pack_start(halign, False, True, 10)
        self.add(vbox)

        self.btn1.connect("clicked", self.selectdate)
        self.btn2.connect("clicked", self.heading)
        self.btn3.connect("clicked", self.dayname)
        self.btn4.connect("clicked", self.bothflags)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def heading(self, widget):
        self.cal.set_display_options(
            Gtk.CalendarDisplayOptions.SHOW_HEADING)

    def dayname(self, widget):
        self.cal.set_display_options(Gtk.CalendarDisplayOptions.SHOW_DAY_NAMES)

    def bothflags(self, widget):
        self.cal.set_display_options(
            Gtk.CalendarDisplayOptions.SHOW_HEADING | Gtk.CalendarDisplayOptions.SHOW_DAY_NAMES)

    def selectdate(self, widget):
        print("Sda")
        tp = self.cal.get_date()
        dialog = Gtk.Dialog("My dialog",
                            self,
                            Gtk.DIALOG_MODAL | Gtk.DIALOG_DESTROY_WITH_PARENT,
                            (Gtk.STOCK_OK, Gtk.RESPONSE_ACCEPT))

        str1 = str(tp[0])
        str2 = str(tp[1]+1)
        str3 = str(tp[2])

        label = Gtk.Label("Date selected:"+str3+"-"+str2+"-"+str1)
        dialog.vbox.add(label)
        label.show()
        res = dialog.run()
        dialog.destroy()
