#
# ScreenStyles.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

style ASInterface_frame:
    background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/FrameChrome.png"], Borders(8,12,8,8), tile=False)
    padding (16, 16)
    xalign 0.5
    yalign 0.5


style ASInterface_vbox is vbox:
    spacing 8

style ASInterface_text:
    font AS_FONTS_DIR + "Regular.ttf"

style ASInterface_button is gui_button
style ASInterface_button_text:
    font AS_FONTS_DIR + "Bold.ttf"

style ASInterfacePushButton is gui_button:
    background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/PushButtonIdle.png"], Borders(20, 8, 20, 8), tile=False)
    hover_background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/PushButtonHover.png"], Borders(20, 8, 20, 8), tile=False)
    padding(20, 8)

style ASInterfacePushButton_text is ASInterface_button_text:
    color "#212121"
    size 16