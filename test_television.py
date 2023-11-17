import pytest
from television import *

def test_power_on_off():
    tv = Television()
    assert not tv._Television__status  # Initially off

    tv.power()
    assert tv._Television__status  # Should be on after toggling power

    tv.power()
    assert not tv._Television__status  # Should be off again

def test_mute_unmute():
    tv = Television()
    tv.power()  # Turn on the TV

    tv.mute()
    assert tv._Television__muted  # Should be muted

    tv.mute()
    assert not tv._Television__muted  # Should be unmuted

def test_channel_up_down():
    tv = Television()
    tv.power()  # Turn on the TV

    initial_channel = tv._Television__channel
    tv.channel_up()
    assert tv._Television__channel == initial_channel + 1  # Channel should increase

    tv.channel_down()
    assert tv._Television__channel == initial_channel  # Channel should return to initial

def test_volume_up_down():
    tv = Television()
    tv.power()  # Turn on the TV

    initial_volume = tv._Television__volume
    tv.volume_up()
    assert tv._Television__volume == initial_volume + 1  # Volume should increase

    tv.volume_down()
    assert tv._Television__volume == initial_volume  # Volume should return to initial

def test_volume_mute_interaction():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.mute()

    tv.volume_up()  # Volume up should unmute
    assert not tv._Television__muted

    tv.mute()  # Mute again
    tv.volume_down()  # Volume down should also unmute
    assert not tv._Television__muted
