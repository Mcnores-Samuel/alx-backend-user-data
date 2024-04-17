#!/usr/bin/env python3
""" Module of Auth views
This module generates the view for the authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication
        Args:
            path (str): the path to check
            excluded_paths (List[str]): the excluded paths

        Returns:
            bool: True if the path is not excluded, False otherwise
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True
    
    def authorization_header(self, request=None) -> str:
        """Returns request object or None"""
        if request:
            return request.header.get('Authorization')
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None
    