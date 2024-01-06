# Stefan's Home Assistant Configuration

[![Build status](https://github.com/stoman/homeassistant-config/actions/workflows/home-assistant.yml/badge.svg)](https://github.com/stoman/homeassistant-config/actions/)
[![MIT license](https://img.shields.io/github/license/stoman/homeassistant-config.svg)](LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/stoman/homeassistant-config.svg)](https://github.com/stoman/homeassistant-config/stargazers/)

This repository contains our configuration for [Home Assistant](https://github.com/home-assistant). It's a collection of small scripts and fun automations for tinkering around and fun.

I hope something can be a useful inspiration for others. If you find this useful, please consider starring this repository: [![GitHub stars](https://img.shields.io/github/stars/stoman/homeassistant-config.svg?style=social)](https://github.com/stoman/homeassistant-config/stargazers/)

## Highlights

- Temperature and humidity sensors for ESP devices: [BME280](esphome/.sensor.bme280.yaml), [DHT22](esphome/.sensor.dht22.yaml)
- [Coffee machine switching on when the toothbrush is used in the morning](automations/coffee.yaml)
- [Waste collection schedule from Abfallwirtschaftsbetrieb München (AWM)](packages/waste_collection_schedule.yaml)
- [Power meter readings via Tasmota](packages/tasmota_smart_meter.yaml) from an EMH ED300S power meter
- [Physical light switches activating Philipps Hue's natural light mode](automations/lights/), because for some reason the official app only supports natural light for manual commands and time triggers, not Hue wall modules...
- [Detection of fridge malfunction](automations/fridge/) in case of suspiciously low power consumption or a switch being disabled

## Hardware

Devices we collected at home include:

- MiniAir 11 running Home Assistant
- FritzBox and Fritz Repeater for Mesh WiFi
- Philipps Hue lights: Centris, Infuse, Ensis, play gradient lightstrips, lightstrips, light bulbs
- Philipps Hue Bridges
- Philipps Hue HDMI Sync Box
- Philipps Hue Motion Sensors
- PHilipps Hue Wall Modules
- Philipps Hue Smart Plug
- Chromecast with Google TV
- Nest Audio
- [ESP32](esphome/.device.esp32.yaml) boards with [BME280](esphome/.sensor.bme280.yaml) sensors
- [ESP8266](esphome/.device.esp8266.yaml) boards with [DHT22](esphome/.sensor.dht22.yaml) sensors
- Roborock S7 Plus
- [Idasen height-adjustable desk](esphome/.sensor.idasen.yaml)
- Raspberry Pi 3B running Pi-hole
- Shelly Plug Plus S for measuring power consumption and Shelly Plug 2 for high wattage devices

## Naming

You will notice that most devices, rooms, sensors, and other entities have German names in this repository. While this produces weird configuration files, that's an intentional choice given that all interfaces at our home are used in German.
