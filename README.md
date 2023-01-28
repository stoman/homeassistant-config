# Stefan's Home Assistant Configuration

[![Build status](https://github.com/stoman/homeassistant-config/actions/workflows/home-assistant.yml/badge.svg)](https://github.com/stoman/homeassistant-config/actions/)
[![MIT license](https://img.shields.io/github/license/stoman/homeassistant-config.svg)](LICENSE.md)
[![GitHub commits](https://badgen.net/github/commits/stoman/homeassistant-config)](https://github.com/stoman/homeassistant-config/commit/)
[![GitHub stars](https://img.shields.io/github/stars/stoman/homeassistant-config.svg)](https://github.com/stoman/homeassistant-config/stargazers/)

This repository contains our configuration for [Home Assistant](https://github.com/home-assistant). It's a collection of small scripts and fun automations for tinkering around and fun.

I hope something can be a useful inspiration for others. If you find this useful, please consider starring this repository: [![GitHub stars](https://img.shields.io/github/stars/stoman/homeassistant-config.svg?style=social)](https://github.com/stoman/homeassistant-config/stargazers/)

## Highlights

- Christmas switch: a lightswitch at home with a Christmas tree icon from the plotter dims the lights, switches on the Christmas tree lights, and plays Christmas music on Spotify.
- Temperature and humidity sensors for ESP devices: [BME280](esphome/.sensor.bme280.yaml), [DHT22](esphome/.sensor.dht22.yaml)
- [Waste collection schedule from Abfallwirtschaftsbetrieb München (AWM)](packages/waste_collection_schedule.yaml)

## Hardware

Devices we collected at home include:

- 1x Raspberry Pi 3B running Home Assistant
- 2x FritzBox and 1x Fritz Repeater for Mesh WiFi
- Philipps Hue lights: 1x Centris, 2x Infuse, 1x Ensis, 1x play gradient lightstrips, 2x lightstrips, 8x light bulbs
- 2x Philipps Hue Bridges
- 1x Philipps Hue HDMI Sync Box
- 3x Philipps Hue Motion Sensors
- 12x PHilipps Hue Wall Modules
- 1x Philipps Hue Smart Plug
- 2x Chromecast with Google TV
- 5x Nest Audio
- 3x [ESP32](esphome/.device.esp32.yaml) boards with [BME280](esphome/.sensor.bme280.yaml) sensors
- 5x [ESP8266](esphome/.device.esp8266.yaml) boards with [DHT22](esphome/.sensor.dht22.yaml) sensors
- 1x Roborock S7 Plus

## Naming

You will notice that most devices, rooms, sensors, and other entities have German names in this repository. While this produces weird configuration files, that's an intentional choice given that all interfaces at our home are used in German.
