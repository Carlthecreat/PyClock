import sys
import datetime as dt
from datetime import datetime
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt, QUrl

SOUND_FILE_PATH = "C:/Users/Chimdiebube/Downloads/clock sound.wav"


def create_grid_layout(rows: int, columns: int, width: int, height: int, Hsizepolicy: QSizePolicy.Policy, Vsizepolicy: QSizePolicy.Policy):
    '''Function to create a grid layout with a specific format as defined by the user.'''
    grid = QGridLayout()
    for row in range(rows):
        for column in range(columns):
            spacer_item = QSpacerItem(width, height, Hsizepolicy, Vsizepolicy)
            grid.addItem(spacer_item, row, column)
    return grid
        
def create_combo_box(num_items: int=None):
    '''Function to create a combo box with a specific number of items.
    Intended for use with combo boxes that hold only numbers, in this case hour and minute values.'''
    combo_box = QComboBox()
    for num in range(num_items):
        combo_box.addItem(str(num).zfill(2))
    return combo_box

class Timer(QWidget):
    '''Timer widget for the clock app. It posesses basic functions such as
    setting a number of hours, minutes or both with the intent to sound an 
    alarm when the time is up.'''
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_alarm_sound_setup()

    def init_ui(self):
        '''Function to setup the layout of the timer widget.'''
        # Setting margins of the base widget.
        self.setContentsMargins(35,20,35,0)

    ##--Grid Layout
        # Initializing the grid layout and setting its dimensions.
        grid = create_grid_layout(rows=4,columns=6,width=40, height=10, Hsizepolicy=QSizePolicy.Policy.Expanding,Vsizepolicy=QSizePolicy.Policy.Expanding)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.setContentsMargins(0,0,0,0)
        grid.setSpacing(10)
        grid.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)

    ##--Widgets
        # Enter Button
        self.enter_button = QPushButton('Enter')
        self.enter_button.setContentsMargins(0,0,0,0)
        self.enter_button.clicked.connect(self.on_click)

        # Reset Button
        self.reset_button = QPushButton('Reset')
        self.reset_button.setContentsMargins(0,0,0,0)
        self.reset_button.setStyleSheet("alignment: center;")
        self.reset_button.clicked.connect(self.reset)

        # Hour Combo Box
        self.hour_combo_box = create_combo_box(24)
        self.hour_combo_box.setContentsMargins(0,0,0,0)

        # Minute Combo Box
        self.minute_combo_box = create_combo_box(60)
        self.minute_combo_box.setContentsMargins(0,0,0,0)

        # Labels
        #-Label postceding the hour combo box-#
        self.hour_label = QLabel('Hour(s)')

        #-Label postceding the minute combo box-#
        self.minute_Label = QLabel('Minute(s)')

        #-Label to display the string 'The timer has been set for:'-#
        self.time_set = QLabel()
        self.time_set.setStyleSheet("font-size: 13px;")

        #-Lable to display the time when the timer will expire.-#
        self.set_time = QLabel()
        self.set_time.setStyleSheet("font-size: 18px;")


        # Adding widgets to layout
        grid.addWidget(self.hour_combo_box, 0, 0, 1, 2) # Order is like this: item, row, column, rowspan, columnspan
        grid.addWidget(self.hour_label, 0, 2)
        grid.addWidget(self.minute_combo_box, 0, 3)
        grid.addWidget(self.minute_Label, 0, 4)
        grid.addWidget(self.enter_button, 0, 5)
        grid.addWidget(self.reset_button, 1, 2, 1, 3)
        grid.addWidget(self.time_set, 2, 2, 1, 3)
        grid.addWidget(self.set_time, 3, 3, 1, 3)

        # Creating timer object
        self.timer = QTimer(self)

        self.setLayout(grid)
    
    def init_alarm_sound_setup(self):
        '''Function to set up the alarm audio'''
        self.alarm_sound = QSoundEffect()
        self.alarm_sound.setSource(QUrl.fromLocalFile(SOUND_FILE_PATH))
        if self.alarm_sound.status() == QSoundEffect.Status.Error:
            print('An error occurred while attempting to load the audio.')
        else:
            self.alarm_sound.setVolume(0.3)

    def on_click(self):
        '''Function that defines actions to be taken when the enter button is clicked.'''
        self.enter_button.setEnabled(False)

        hour = self.hour_combo_box.currentText()
        minute =  self.minute_combo_box.currentText()
        
        # Variables to store the current time and the length of the timer duration.
        current_time = datetime.now()
        timer_duration = dt.timedelta(hours=int(hour), minutes=int(minute))

        # Variables for the future time (when the timer expires) and the formatted future time.
        self.future_time = current_time + timer_duration
        future_time_frmatted = self.future_time.strftime("%H:%M")

        # Setting the labels to display the moment when the timer expires.
        self.time_set.setText('The timer has been set for:')
        self.set_time.setText(str(future_time_frmatted))

        # Connect the timer to another function to check the time every second.
        self.timer.timeout.connect(self.check_time)
        self.timer.start(1000)

    def check_time(self):
        '''Function to check the time and see whether it matches with the set duration on the timer.'''
        current_time = datetime.now()
        if current_time >= self.future_time:
            print('Time to wake up')
            self.alarm_sound.play()
            self.timer.stop()

    def reset(self):
        '''Function for the actions to be taken for different scenarios when the reset button is pressed.'''
        self.time_set.setText('')
        self.set_time.setText('')
        self.hour_combo_box.setCurrentIndex(0)
        self.minute_combo_box.setCurrentIndex(0)

        # If the timer is active.
        if self.timer.isActive():
            self.timer.stop()

        # If the alarm is playing.
        elif self.alarm_sound.isPlaying():
            self.alarm_sound.stop()

        # If the enter button is disabled.
        if not self.enter_button.isEnabled():
            self.enter_button.setEnabled(True)

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.centisecond = 0
        self.second = 0
        self.minute = 0
        self.hour = 0

############----Primary and Secondary Layouts----############
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        ##--Button Layout--##
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

############----Label Objects----############
        self.name_label = QLabel('Stopwatch')
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.stopwatch_time_label = QLabel()
        self.stopwatch_time_label.setTextFormat(Qt.TextFormat.RichText)
        self.stopwatch_time_label.setText(f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}:{str(self.centisecond).zfill(2)}')
        self.stopwatch_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

############----Timer Object----#############
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start)

############----Button Objects----############
        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stop')
        self.reset_button = QPushButton('Reset')

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

############----Setting layout and adding widgets----############
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.stopwatch_time_label)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.stop_button)
        self.button_layout.addWidget(self.reset_button)

    def start(self):
        self.timer.start(10)
        self.centisecond += 1
        if self.centisecond == 100:
            self.centisecond = 0
            self.second += 1
            if self.second == 60:
                self.second = 0
                self.minute += 1
                if self.minute == 60:
                    self.minute = 0
                    self.hour += 1
                    if self.hour == 24:
                        self.centisecond = 0
                        self.second = 0
                        self.minute = 0
                        self.hour = 0
        self.stopwatch_time_label.setText(f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}:{str(self.centisecond).zfill(2)}')
        self.start_button.setEnabled(False)

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
        self.start_button.setEnabled(True)
    
    def reset(self):
        self.centisecond = 0
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.stopwatch_time_label.setText(f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}:{str(self.centisecond).zfill(2)}')
        self.timer.stop()
        if not self.start_button.isEnabled():
            self.start_button.setEnabled(True)
            
            
class Clock(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QVBoxLayout()

        self.date_label = QLabel()
        self.current_time()

        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.date_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.current_time)
        self.timer.start(1000)
    
    def current_time(self):
        time = datetime.now()
        date = time.strftime("%A, %B %d")
        hour_minute_f = time.strftime("%H:%M %p")
        self.date_label.setText(f'''
{date}
{hour_minute_f}''')
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Alarm Clock')
        self.setStyleSheet('''font-family: "Consolas";''')
        self.x = 50
        self.y = 60

        self.main_layout = QVBoxLayout()
        self.setFixedSize(400,200)

        # Navigation Bar Layout
        self.nav_layout = QHBoxLayout()
        self.stopwatch_button = QPushButton('Stopwatch')
        self.clock_button = QPushButton('Clock')
        self.timer_button = QPushButton('Timer')
        self.nav_layout.addWidget(self.stopwatch_button)
        self.nav_layout.addWidget(self.clock_button)
        self.nav_layout.addWidget(self.timer_button)
        self.main_layout.addLayout(self.nav_layout)

        # Create a stacked window object
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Initialize the Stopwatch and Clock Classses
        self.stopwatch_widget = Stopwatch()
        self.clock_widget = Clock()
        self.timer_widget = Timer()

        # Add clock and stopwatch to stacked widget object
        self.stacked_widget.addWidget(self.stopwatch_widget)
        self.stacked_widget.addWidget(self.clock_widget)
        self.stacked_widget.addWidget(self.timer_widget)

        # Connect the buttons to their functions
        self.clock_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.clock_widget))
        self.stopwatch_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.stopwatch_widget))
        self.timer_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.timer_widget))

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()