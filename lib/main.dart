import 'package:flutter/material.dart';
import 'package:go_moon/pages/home_page.dart';
import 'dart:ui' show lerpDouble;

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GoMoon',
      theme:
          ThemeData(scaffoldBackgroundColor: Color.fromRGBO(31, 31, 31, 1.3)),
      home: HomePage(),
    );
  }
}
