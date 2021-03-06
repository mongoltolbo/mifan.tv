#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2013 tuila.me

from wtforms import TextField, HiddenField, validators
from lib.forms import Form

class ReplyForm(Form):
    content = TextField('Content', [
        validators.Required(message = "请填写回复内容"),
    ])

    tid = TextField('Tid', [
        validators.Required(message = "要回复的帖子不明确"),
    ])

class PostForm(Form):
    intro = TextField('Intro', [
        validators.Required(message = "请填写视频介绍"),
        validators.Length(min = 3, message = "介绍长度过短（3-56个字符）"),
        validators.Length(max = 156, message = "介绍长度过长（3-56个字符）"),
    ])

    link = TextField('Link', [
        validators.Required(message = "请填写视频链接"),
    ])

    channel = TextField('Channel', [
        validators.Required(message = "请填写视频频道"),
    ])

class PostForm2(Form):
    intro = TextField('Intro', [
        validators.Required(message = "请填写视频介绍"),
        validators.Length(min = 3, message = "介绍长度过短（3-56个字符）"),
        validators.Length(max = 156, message = "介绍长度过长（3-56个字符）"),
    ])

    link = TextField('Link', [
        validators.Required(message = "请填写视频链接"),
    ])

class ChannelForm(Form):
    intro = TextField('Intro', [
        validators.Required(message = "请填写频道介绍"),
        validators.Length(min = 3, message = "介绍长度过短（3-56个字符）"),
        validators.Length(max = 156, message = "介绍长度过长（3-56个字符）"),
    ])

    name = TextField('Name', [
        validators.Required(message = "请填写频道名称"),
    ])

    avatar = TextField('Avatar', [
        validators.Required(message = "请填写频道头像图片链接"),
    ])

class ReplyEditForm(Form):
    content = TextField('Content', [
        validators.Required(message = "请填写回复内容"),
    ])

class CreateMessageForm(Form):
    content = TextField('Content', [
        validators.Required(message = "请填写帖子内容"),
    ])