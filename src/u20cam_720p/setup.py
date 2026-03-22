import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'u20cam_720p'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hardli',
    maintainer_email='lijialei829@gmail.com',
    description='Camera package for u20cam 720p',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = u20cam_720p.live_stream_camera:main',
        ],
    },
)
