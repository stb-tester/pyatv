"""Functional tests for Airplay."""
import math

from aiohttp import ClientSession
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import pytest

from pyatv import exceptions, net
from pyatv.airplay import player
from pyatv.const import Protocol

from tests.fake_device import FakeAppleTV
from tests.utils import _fake_sleep, stub_sleep, total_sleep_time, unstub_sleep

STREAM = "http://airplaystream"
START_POSITION = 0.8

pytestmark = pytest.mark.asyncio


@pytest.fixture(name="airplay_player")
def airplay_player_fixture(client_connection):
    yield player.AirPlayPlayer(client_connection)


async def test_play_video(airplay_usecase, airplay_player, airplay_state):
    airplay_usecase.airplay_playback_idle()
    airplay_usecase.airplay_playback_playing()
    airplay_usecase.airplay_playback_idle()

    await airplay_player.play_url(STREAM, position=START_POSITION)

    assert airplay_state.last_airplay_url == STREAM
    assert airplay_state.last_airplay_start == START_POSITION
    assert airplay_state.last_airplay_uuid is not None
    assert math.isclose(total_sleep_time(), 2.0)


async def test_play_video_no_permission(airplay_usecase, airplay_player):
    airplay_usecase.airplay_playback_playing_no_permission()

    with pytest.raises(exceptions.AuthenticationError):
        await airplay_player.play_url(STREAM, position=START_POSITION)


async def test_play_with_retries(airplay_usecase, airplay_player, airplay_state):
    airplay_usecase.airplay_play_failure(2)
    airplay_usecase.airplay_playback_playing()
    airplay_usecase.airplay_playback_idle()

    await airplay_player.play_url(STREAM, position=START_POSITION)

    assert airplay_state.play_count == 3


async def test_play_with_too_many_retries(airplay_usecase, airplay_player):
    airplay_usecase.airplay_play_failure(10)
    airplay_usecase.airplay_playback_playing()
    airplay_usecase.airplay_playback_idle()

    with pytest.raises(exceptions.PlaybackError):
        await airplay_player.play_url(STREAM, position=START_POSITION)