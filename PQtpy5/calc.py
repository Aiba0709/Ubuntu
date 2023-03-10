<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>654</width>
    <height>744</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QDialogButtonBox" name="buttonBox">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>600</y>
     <width>341</width>
     <height>32</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
   <property name="standardButtons">
    <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>0</y>
     <width>161</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 21pt &quot;MS Shell Dlg 2&quot;;
text-decoration: underline;</string>
   </property>
   <property name="text">
    <string>GeekTech</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>60</y>
     <width>141</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 18pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>Kalculator</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="input1">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>120</y>
     <width>191</width>
     <height>22</height>
    </rect>
   </property>
   <property name="placeholderText">
    <string>           Первая цифра</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="input2">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>160</y>
     <width>181</width>
     <height>22</height>
    </rect>
   </property>
   <property name="placeholderText">
    <string>            Вторая цифра</string>
   </property>
  </widget>
  <widget class="QPushButton" name="add">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>200</y>
     <width>93</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 14pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>+</string>
   </property>
  </widget>
  <widget class="QPushButton" name="sub">
   <property name="geometry">
    <rect>
     <x>320</x>
     <y>200</y>
     <width>93</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 14pt &quot;MS Shell Dlg 2&quot;;
font: 20pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>-</string>
   </property>
  </widget>
  <widget class="QPushButton" name="muit">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>280</y>
     <width>93</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">

font: 20pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>*</string>
   </property>
  </widget>
  <widget class="QPushButton" name="div">
   <property name="geometry">
    <rect>
     <x>320</x>
     <y>280</y>
     <width>93</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 14pt &quot;MS Shell Dlg 2&quot;;
font: 20pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>/</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_3">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>370</y>
     <width>181</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 14pt &quot;MS Shell Dlg 2&quot;;
font: 75 14pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="placeholderText">
    <string>        Резуультат</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>buttonBox</sender>
   <signal>accepted()</signal>
   <receiver>Dialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>248</x>
     <y>254</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>buttonBox</sender>
   <signal>rejected()</signal>
   <receiver>Dialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>316</x>
     <y>260</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
