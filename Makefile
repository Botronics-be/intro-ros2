.PHONY: build

release:
	colcon build --cmake-args=-DCMAKE_BUILD_TYPE=Release

install-deps:
	rosdep install -i --from-path src --rosdistro humble -y

run-talker:
	ros2 run talker first_talker

run-listener:
	ros2 run listener first_listener 

get-repos:
	vcs import src --recursive < my.repos 

run-camera:
	ros2 launch zed_wrapper zed2i.launch.py

run-qr-code:
	ros2 run zbar_ros barcode_reader --ros-args --remap image:=/zed2i/zed_node/rgb/image_rect_color

build:
	colcon build --symlink-install

clean:
	rm -rf build install log

rviz:
	rviz2 -d src/listener/config/config.rviz
