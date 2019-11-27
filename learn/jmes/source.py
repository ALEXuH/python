# -*- coding: UTF-8 -*-
source = {"a" : {"b" : {"c" : ["da", "dd", "aa"]}}}

source1= {"a": {
    "b": {
        "c": [
            {"d": [0, [1, 2]]},
            {"d": [3, 4]}
        ]
    }
}}

source2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

source3 = {
    "people": [
        {"first": "James", "last": "d"},
        {"first": "Jacob", "last": "e"},
        {"first": "Jayden", "last": "f"},
        {"missing": "different"}
    ],
    "foo": {"bar": "baz"}
}

source4 = {
    "ops": {
        "functionA": {"numArgs": 2},
        "functionB": {"numArgs": 3},
        "functionC": {"variadic": "true"}
    }
}

source5 = {
    "reservations": [
        {
            "instances": [
                {"state": "running"},
                {"state1": "stopped"}
            ]
        },
        {
            "instances": [
                {"state": "terminated"},
                {"state1": "runnning"}
            ]
        }
    ]
}

source6 = {
    "machines": [
        {"name": "a", "state": "running"},
        {"name": "b", "state": "stopped"},
        {"name": "b", "state": "running"}
    ]
}

source7 = {
    "people": [
        {
            "name": "a",
            "state": {"name": "up"}
        },
        {
            "name": "b",
            "state": {"name": "down"}
        },
        {
            "name": "c",
            "state": {"name": "up"}
        }
    ]
}

source8 = {
    "people": [
        {
            "age": 20,
            "other": "foo",
            "name": "Bob"
        },
        {
            "age": 25,
            "other": "bar",
            "name": "Fred"
        },
        {
            "age": 30,
            "other": "baz",
            "name": "George"
        }
    ]
}

source9 = {
    "Contents": [
        {
            "Date": "2014-12-21T05:18:08.000Z",
            "Key": "logs/bb",
            "Size": 303
        },
        {
            "Date": "2014-12-20T05:19:10.000Z",
            "Key": "logs/aa",
            "Size": 308
        },
        {
            "Date": "2014-12-20T05:19:12.000Z",
            "Key": "logs/qux",
            "Size": 297
        },
        {
            "Date": "2014-11-20T05:22:23.000Z",
            "Key": "logs/baz",
            "Size": 329
        },
        {
            "Date": "2014-12-20T05:25:24.000Z",
            "Key": "logs/bar",
            "Size": 604
        },
        {
            "Date": "2014-12-20T05:27:12.000Z",
            "Key": "logs/foo",
            "Size": 647
        }
    ]
}

source10 = {
    "locations": [
        {"name": "Seattle", "state": "WA"},
        {"name": "New York", "state": "NY"},
        {"name": "Bellevue", "state": "WA"},
        {"name": "Olympia", "state": "WA"}
    ]
}

source11 = {
    "took": 0,
    "timed_out": False,
    "_shards": {
        "total": 5,
        "successful": 5,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": 12140,
        "max_score": 1,
        "hits": [
            {
                "_index": "device_index",
                "_type": "device",
                "_id": "district.94cc78d9615c4bad8fe9aec2bf16abb9",
                "_score": 1,
                "_source": {
                    "deviceType": "CityCam",
                    "data": {
                        "address": "保德路454号向西",
                        "town": {
                            "areaID": 2,
                            "areaName": "临汾路街道",
                            "areaCategory": "街道"
                        },
                        "vedio_type": "rtmp",
                        "areaCategory": "小区",
                        "isSensor": False,
                        "visual_area": [],
                        "area_district": {
                            "areaID": 39,
                            "areaName": "静安区",
                            "areaCategory": "区"
                        },
                        "video_type": "rtmp",
                        "playback_url_enable": False,
                        "installedPlace": {
                            "areaID": -2,
                            "areaName": "_道路",
                            "areaCategory": "点位"
                        },
                        "exists": True,
                        "camera_resolution_ratio": "123x234",
                        "location": {
                            "lon": 121.45368165,
                            "lat": 31.3192256672
                        },
                        "playback_url": "rtmp://10.3.81.10:1935/domain=31010601011320000008&resource=31010601011320000040-0&quality=2&src=0"
                    },
                    "channel": "district",
                    "messageClass": "device",
                    "camera_resolution_ratio": "123x234",
                    "deviceID": "district.94cc78d9615c4bad8fe9aec2bf16abb9"
                }
            },
            {
                "_index": "device_index",
                "_type": "device",
                "_id": "district.5d3208a0dde6457d9708d7e89fe38bbb",
                "_score": 1,
                "_source": {
                    "deviceType": "CityCam",
                    "data": {
                        "address": "江杨临汾西北侧",
                        "town": {
                            "areaID": 2,
                            "areaName": "临汾路街道",
                            "areaCategory": "街道"
                        },
                        "vedio_type": "rtmp",
                        "areaCategory": "小区",
                        "isSensor": True,
                        "visual_area": [],
                        "area_district": {
                            "areaID": 39,
                            "areaName": "静安区",
                            "areaCategory": "区"
                        },
                        "video_type": "rtmp",
                        "playback_url_enable": True,
                        "installedPlace": {
                            "areaID": -2,
                            "areaName": "_道路",
                            "areaCategory": "点位"
                        },
                        "exists": True,
                        "camera_resolution_ratio": "123x234",
                        "location": {
                            "lon": 121.463179005,
                            "lat": 31.3129932774
                        },
                        "playback_url": "rtmp://10.3.81.10:1935/domain=31010601012000000000&resource=31010601011320000121-0&quality=2&src=1"
                    },
                    "channel": "district",
                    "messageClass": "device",
                    "camera_resolution_ratio": "123x234",
                    "deviceID": "district.5d3208a0dde6457d9708d7e89fe38bbb"
                }
            }
        ]
    }
}