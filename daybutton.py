#!/usr/bin/env python3
from gi.repository import Gtk, Gdk
import gi
gi.require_version("Gtk", "3.0")


class DayButtonGroup():
    def __init__(self, callback):
        self.daybuttons: list = []
        self.call = callback

    def add_button(self, day_button):
        self.daybuttons.append(day_button)
        day_button.connect("toggled", self.on_button_toggled, "")

    def on_button_toggled(self, button, name):
        # briefly disconnect
        for day_button in self.daybuttons:
            day_button.disconnect_by_func(self.on_button_toggled)
            if day_button == button:
                day_button.set_active(True)
                self.call(day_button.date)
            else:
                day_button.set_active(False)

            day_button.connect("toggled", self.on_button_toggled, "")

    def clear(self):
        for b in self.daybuttons:
            b.disconnect_by_func(self.on_button_toggled)
        self.daybuttons.clear()


class DayButton(Gtk.ToggleButton):
    def __init__(self, date, today):
        self.date = date
        self.today = today
        Gtk.ToggleButton.__init__(self, "%i" % (date.day))
        self.set_name('daybutton')
        if date.day == self.today.day and date.month == self.today.month and date.year == self.today.year:
            self.set_active(True)
            self.set_name('daybutton-selected')

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, DayButton):
            return self.date == other.date
        return False
