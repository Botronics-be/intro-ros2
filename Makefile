.PHONY: build

release:
	colcon build

install-deps:
	rosdep install -i --from-path src --rosdistro humble -y

run-talker:
	ros2 run talker first_talker

run-listener:
	ros2 run listener first_listener 

build:
	colcon build --symlink-install