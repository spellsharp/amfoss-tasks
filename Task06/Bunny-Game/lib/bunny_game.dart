import 'dart:ui';

import 'package:flame/components.dart';
import 'package:flame/game.dart';
import 'package:flame/input.dart';
import 'package:flutter/services.dart';
import 'bunny.dart';
import 'background.dart';
import 'package:flutter/material.dart';

import 'directions.dart';

class BunnyGame extends FlameGame with KeyboardEvents {
  Bunny _bunny = Bunny();
  Background _background = Background();

  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_background);
    await add(_bunny);
    _bunny.position = _background.size / 1.5;
    camera.followComponent(_bunny,
        worldBounds:
            Rect.fromLTRB(0, 0, _background.size.x, _background.size.y));
  }

  onArrowKeyChanged(Direction direction) {
    _bunny.direction = direction;
  }
}
