import sys
from vars import *
from outsideclient import GetWord 
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QSizePolicy,
    QSpacerItem,
    QToolBar,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QFrame,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QStatusBar,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPlainTextEdit,
    QScrollArea

)


class MainResultWindow(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, *args, **kwargs):
        super(SingleResult, self).__init__(*args, **kwargs)

class ExampleEntry(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, example, *args, **kwargs):
        super(ExampleEntry, self).__init__(*args, **kwargs)
        exampleWrap = QHBoxLayout()
        leftSideOg = QLabel(example.src)
        rightSideOg = QLabel(example.dst)
        leftSideOg.setStyleSheet(window.colorscheme['standardFont'])
        rightSideOg.setStyleSheet(window.colorscheme['standardFont'])
        leftSideOg.setWordWrap(True)
        rightSideOg.setWordWrap(True)
        exampleWrap.addWidget(leftSideOg)
        exampleWrap.addWidget(rightSideOg)
        exampleWrap.setContentsMargins(40, 0, 0, 0)
        self.setLayout(exampleWrap)
                
class FeaturedTranslation(QFrame):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, translation, *args, **kwargs):
        super(FeaturedTranslation, self).__init__(*args, **kwargs)  
        self.setContentsMargins(40, 0, 0, 0)
        
        #Modify in a more native way the color of the border
        pal = self.palette()
        pal.setColor(QPalette.WindowText, QColor(window.colorscheme["currentlyOnBorder"]))
        self.setPalette(pal)

        # This appends the translation instance to the list used to go through the translations 
        window.browsableReferences.append(self)
        translationContainer = QVBoxLayout()
        translationWordLabel = QLabel(translation.text)
        translationWordLabel.setStyleSheet(window.colorscheme['featuredTranslationWordLabel'])
        translationContainer.addWidget(translationWordLabel)
        bottomExamplesContainer = QVBoxLayout()
        for example in translation.examples:
            bottomExamplesContainer.addWidget(ExampleEntry(example))
        translationContainer.addLayout(bottomExamplesContainer)
        self.setLayout(translationContainer)

    def highlight(self):
        self.setFrameShape(QFrame.Box)  # set the frame shape to a box
        self.setLineWidth(3)  # set the line width of the box
        window.scroll_area.ensureWidgetVisible(self)
    def unhighlight(self):
        self.setFrameShape(QFrame.NoFrame)  # set the frame shape to a box
        self.setLineWidth(0)  # set the line width of the box


class NonFeaturedTranslations(QWidget):
    def __init__(self, translations, *args, **kwargs):
        super(NonFeaturedTranslations, self).__init__(*args, **kwargs)
        nonContainer = QVBoxLayout()
        nonContainer.setContentsMargins(40, 20, 0, 0)
        infoHeader = QLabel("Less common")
        infoHeader.setStyleSheet(window.colorscheme['lessCommonHeader'])
        translationsList = FlowLayout()        

        for translation in translations:
            wordLabel = QLabel(translation.text)
            wordLabel.setStyleSheet(window.colorscheme['lessCommonTranslation'])
            wordLabel.setContentsMargins(0,0,20,0)
            translationsList.addWidget(wordLabel)
        nonContainer.addWidget(infoHeader)
        nonContainer.addLayout(translationsList)
        self.setLayout(nonContainer)


class TranslationSection(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, ogType, ogWord, translations, *args, **kwargs):
        super(TranslationSection, self).__init__(*args, **kwargs)
        topLayer = QVBoxLayout()
        ogWrap = QHBoxLayout()
        ogWordLabel, ogTypeLabel = QLabel(ogWord), QLabel(ogType)
        ogWordLabel.setStyleSheet(window.colorscheme['ogWordLabel'])
        ogTypeLabel.setStyleSheet(window.colorscheme['ogTypeLabel'])
        ogWrap.addWidget(ogWordLabel)
        ogWrap.addWidget(ogTypeLabel)
        ogWrap.setAlignment(Qt.AlignLeft)
        self.translationsLayer = QVBoxLayout() 
        topLayer.addLayout(ogWrap)
        # Now it's Featured Translations
        for translation in filter(lambda t : t.featured == True, translations):
                self.translationsLayer.addWidget(FeaturedTranslation(translation))
        nonFeaturedList = list(filter(lambda t : t.featured == False, translations))
        if len(nonFeaturedList) > 0: self.translationsLayer.addWidget(NonFeaturedTranslations(nonFeaturedList))
        topLayer.addLayout(self.translationsLayer)
        self.setLayout(topLayer)
    
    def switchColorscheme(self,colorscheme):
        self.setStyleSheet(colorscheme['windowBg'])
        self.mainQueryEdit.setStyleSheet(colorscheme['mainQuery'])

        
        



class SingleResult(QFrame):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, dupa, *args, **kwargs):
        super(SingleResult, self).__init__(*args, **kwargs)
        print(dupa)
        outerLayout = QVBoxLayout()
        self.mainResultTitle = QLabel("Unregelmäßig")
        translationsLayout = QHBoxLayout()
        a = ['irregular', 'uneven', 'sporadic']
        for i in a:
            translationsLayout.addWidget(QLabel(i))

        outerLayout.addWidget(self.mainResultTitle)
        outerLayout.addLayout(translationsLayout)

        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Plain)
        self.setLayout(outerLayout)


    def return_pressed(self):
        print("Return pressed!")

class MainInput(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, *args, **kwargs):
        super(MainInput, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        layoutResults = QVBoxLayout()
        self._lineEdit = QLineEdit()
        self._lineEdit.returnPressed.connect(self.return_pressed)
        layoutResults.setAlignment(Qt.AlignBottom)

        layout.addWidget(self._lineEdit)
        layout.addLayout(layoutResults)
        self.setLayout(layout)
    def return_pressed(self):
        print("Return pressed!")

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linguee-Front") 
        
        #state variables
        self.vals = []
        self.currentQuery = None
        self.mode = "s"
        self.browsableReferences = []
        self.currentlyOn = 0
        self.colorscheme = blackColorscheme
        
        #this just prepares some basic functionality like scrollablity
        self.scroll_area = QScrollArea()
        self.mainWidget = QWidget()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.mainWidget)
        layout = QVBoxLayout(self.mainWidget)
        
        self.createStatusbar()
        self.createToolbar()
        self.setCentralWidget(self.scroll_area)
        self.switchColorscheme(blackColorscheme)
    
    def createStatusbar(self):
        # you need to disable toolbar's movability
        statusbar = QStatusBar()
        self.statusOutput = QLabel("")
        self.modeLabel = QLabel("Search")
        self.modeLabel.setStyleSheet(searchStyle)
        statusbar.addWidget(self.modeLabel)
        statusbar.addWidget(self.statusOutput)
        self.setStatusBar(statusbar)

        
    def createToolbar(self):
        # Creating toolbar elements
        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.mainQueryEdit = QLineEdit()
        self.mainQueryEdit.returnPressed.connect(lambda: self.updateUi(self.mainQueryEdit.text()))
        self.mainQueryEdit.focusInEvent = self.switchMode
        self.mainQueryEdit.focusOutEvent = self.switchMode
        self.toolbar.addWidget(self.mainQueryEdit)
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)

    def switchMode(self, event):
        #This first condition is in order to preserve state between switching windows
        if event.reason() == Qt.FocusReason.ActiveWindowFocusReason :
            if self.mode == "b":
                self.mainQueryEdit.clearFocus()
            else:
                self.mainQueryEdit.setFocus()
        else:
            if event.gotFocus():
                self.mode = "s"
                self.modeLabel.setText("Search")
                self.modeLabel.setStyleSheet(searchStyle)
            elif event.lostFocus():
                self.browsableReferences[self.currentlyOn].highlight()
                self.mode = "b"
                self.modeLabel.setText("Browse")
                self.modeLabel.setStyleSheet(browseStyle)

    def keyPressEvent(self, event):
        # this function handles every global keybinding
        
        if event.key() == Qt.Key_I or event.key() == Qt.Key_A:
            if self.previousD:
                self.mainQueryEdit.clear()
            self.mainQueryEdit.setFocus()
        elif event.key() == Qt.Key_Escape:
            self.mainQueryEdit.clearFocus()
        elif event.key() == Qt.Key_J:
            # adjusted for indexing
            self.moveOn(1)
        elif event.key() == Qt.Key_K:
            # adjusted for indexing
            self.moveOn(-1)
        elif event.key() == Qt.Key_G and event.modifiers() == Qt.ShiftModifier:
            self.moveTo("down")
        elif event.key() == Qt.Key_G:
            if self.previousG == None:
                self.previousG = True
            else:
                self.moveTo('up')
        elif event.key() == Qt.Key_C:
            self.switchColorscheme(whiteColorscheme) if self.colorscheme == blackColorscheme else self.switchColorscheme(blackColorscheme)
        elif event.key() == Qt.Key_D:
            if self.previousD == None:
                self.previousD = True
        else:
            self.previousG = None
            self.previousD = None

    def moveOn(self,direction):
        if self.currentlyOn+direction < len(self.browsableReferences) and self.currentlyOn+direction > -1:
            self.browsableReferences[self.currentlyOn].unhighlight()
            self.currentlyOn+=direction
            self.browsableReferences[self.currentlyOn].highlight()

    def moveTo(self,direction):
        self.browsableReferences[self.currentlyOn].unhighlight()
        if direction == "down":
            self.currentlyOn=len(self.browsableReferences) - 1
        else:
            self.currentlyOn=0
        self.browsableReferences[self.currentlyOn].highlight()
    
    def switchColorscheme(self,colorscheme):
        self.colorscheme = colorscheme
        self.setStyleSheet(colorscheme['windowBg'])
        self.mainQueryEdit.setStyleSheet(colorscheme['mainQuery'])
        self.statusOutput.setStyleSheet(self.colorscheme["standardFont"])
        if self.currentQuery != None: self.updateUi(self.currentQuery)
            

    def updateStatusbar(self, correctedQuery):
        self.statusOutput.setText(f"{self.currentQuery} → {correctedQuery}")

    def updateUi(self, word):
        apiResponse = GetWord(word)
        self.vals = apiResponse.lemmas
        self.currentQuery = word
        if apiResponse.query != apiResponse.correct_query: 
            self.updateStatusbar(apiResponse.correct_query)
        else:
            self.statusOutput.setText("")
        layout = self.mainWidget.layout()
        # reset references
        self.browsableReferences = []
         
        while layout.count() > 0:
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
        for i in self.vals:
            layout.addWidget(TranslationSection(i.pos, i.text, i.translations)) 
        layout.addStretch()

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
font = app.font()
font.setPointSize(14)
app.setFont(font)


window = MainWindow()

window.show()

app.exec()


