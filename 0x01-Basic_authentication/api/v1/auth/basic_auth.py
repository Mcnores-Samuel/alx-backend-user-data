#!/usr/bin/env python3
"""This module contains the basic authentication logic for the API"""
from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return
        if not isinstance(base64_authorization_header, str):
            return
        try:
            credentials = base64_authorization_header.encode('utf-8')
            credentials = b64decode(credentials)
            credentials = credentials.decode('utf-8')
        except Exception:
            return None
        return credentials

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from the
        Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return(None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' in decoded_base64_authorization_header:
            credentials = decoded_base64_authorization_header.split(":")
            return (credentials[0], credentials[1])
        return (None, None)
