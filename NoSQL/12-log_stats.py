#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB

This script connects to a MongoDB database and displays statistics
about nginx log entries including total logs, HTTP methods counts,
and status check requests.
"""


from pymongo import MongoClient


if __name__ == "__main__":
    """
    Main execution block that connects to MongoDB and displays
    nginx log statistics including:
    - Total number of logs
    - Count per HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of status check requests (GET /status)
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    get_method = collection.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get_method}")
    post_method = collection.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post_method}")
    put_method = collection.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put_method}")
    patch_method = collection.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch_method}")
    delete_method = collection.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete_method}")
    total_check = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total_check} status check")
