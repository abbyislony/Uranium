// Copyright (c) 2015 Ultimaker B.V.
// Uranium is released under the terms of the AGPLv3 or higher.

import QtQuick 2.1
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1

CheckBox
{
    signal valueChanged(bool value);
    id: base
    checked: boolCheck(value) //From parent loader
    onCheckedChanged: valueChanged(checked);
    function boolCheck(value) //Hack to ensure a good match between python and qml.
    {
        if(value == "True")
        {
            return true
        }else if(value == "False")
        {
            return false
        }
        else
        {
            return value
        }
    }
    style: CheckBoxStyle
    {
        background: Item { }
        label: Label{ }
        indicator: Rectangle
        {
            implicitWidth:  control.height;
            implicitHeight: control.height;

            color:
            {
                if(control.hovered || base.activeFocus)
                {
                    return itemStyle.controlHighlightColor
                }
                else
                {
                    return itemStyle.controlColor
                }
            }
            border.width: itemStyle.controlBorderWidth;
            border.color: itemStyle.controlBorderColor;

            Label
            {
                anchors.centerIn: parent;
                color: itemStyle.controlTextColor;
                font: itemStyle.controlFont;

                text: "✓";

                opacity: control.checked
                Behavior on opacity { NumberAnimation { duration: 100; } }
            }
        }
    }
}
