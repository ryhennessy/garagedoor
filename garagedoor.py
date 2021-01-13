#!/usr/bin/python3
import os
import argparse
from aladdin_connect import AladdinConnectClient



if __name__ == '__main__':
    client = AladdinConnectClient(os.environ['GARAGE_LOGIN'], os.environ['GARAGE_PASSWD'])
    client.login()

    parser = argparse.ArgumentParser(description="Simple script to open and close doors in the Hennessy household.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--close", action="store", help="Close the specified garage door")
    group.add_argument("-o", "--open", action="store", help="Open the specified garage door")
    group.add_argument("-s", "--status", action="store_true", help="Get status on both doors")
    args = parser.parse_args()
    garage_id=client.get_doors()[0]['device_id']

    if args.status:
        print("-."*30)
        print("Kelly's Garage Door is ", client.get_door_status(garage_id, 1), ".", sep="")
        print("Ryan's Garage Door is ", client.get_door_status(garage_id, 2), ".", sep="")
        print("-."*30)

    elif args.close != None:
        if args.close.title() == "Kelly":
            garage_door = 1
        else:
            garage_door = 2
        client.close_door(garage_id,garage_door)

    elif args.open != None:
        if args.open.title() == "Kelly":
            garage_door = 1
        else:
            garage_door = 2
        client.open_door(garage_id,garage_door)
