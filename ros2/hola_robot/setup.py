from setuptools import setup

package_name = 'hola_robot'

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
    maintainer='Raul Lara',
    maintainer_email='raul.lara@upm.es',
    description='Primer paquete de la asignatura robótica de la ETSISI. Solo incluye un nodo.',
    license='GPL',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hola-robot = hola_robot.robotito:main"
        ],
    },
)
