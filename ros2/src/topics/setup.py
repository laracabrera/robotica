from setuptools import setup

package_name = 'topics'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raúl Lara',
    maintainer_email='raul.lara@upm.es',
    description='Prueba de concepto de los topics de ROS2',
    license='GPL',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "emisor = topics.emisor:main",
            "receptor = topics.receptor:main"
        ],
    },
)
