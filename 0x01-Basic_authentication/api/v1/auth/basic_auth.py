#!/usr/bin/env python3
"""This module contains the basic authentication logic for the API"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class to manage the API authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""

        if authorization_header is None:
            return
        if not isinstance(authorization_header, str):
            return
        if not authorization_header.startswith('Basic '):
            return
        return authorization_header.split(' ')[1]
