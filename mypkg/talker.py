# SPDX-FileCopyrightText: 2023 Tougo Kataita 　　　　　
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "片板柊吾":
        response.age = 44
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
