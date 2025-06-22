#!/usr/bin/env python3
# encoding: utf-8

from islendingabok import IslendingabokAPI
import argparse
import os


def main(username, password):
    api = IslendingabokAPI(username, password)
    user_info = api.me()

    print(user_info['name'])

    results = api.find(u'Vigdís Finnbogadóttir')

    for person_info in results:
        print(person_info['name'], person_info['dob'], person_info['id'])

    oli_stef = api.find(u'Ólafur Indriði Stefánsson', 1973, 7)

    oli_stef_id = oli_stef[0]["id"]

    siblings_of_oli_stef = api.siblings(oli_stef_id)

    for sibling in siblings_of_oli_stef:
        print(sibling["name"])


def parse_arguments():
    parser = argparse.ArgumentParser(description='Connects to Islendingabok and accesses user data.')
    parser.add_argument('--username', default=os.getenv('ISL_USER'),
        help='username on Islendingabok (defaults to ISL_USER env variable)')
    parser.add_argument('--password', default=os.getenv('ISL_PASSWORD'),
        help='password on Islendingabok (defaults to ISL_PASSWORD env variable)')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    print(args.username, args.password)

    main(args.username, args.password)
