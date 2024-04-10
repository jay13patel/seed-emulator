FROM python:3.7-slim
ARG DEBIAN_FRONTEND=noninteractive
# Install software-properties-common to easily add new repositories
COPY carla/agents /carla/agents
COPY get_car.py /carla/get_car.py
COPY refactor_automatic_control.py /carla/refactor_automatic_control.py
COPY requirements.txt /carla/requirements.txt
RUN chmod +x /carla/refactor_automatic_control.py
RUN chmod +x /carla/get_car.py
RUN pip install --no-cache-dir -r /carla/requirements.txt
ENTRYPOINT ["python", "/carla/refactor_automatic_control.py"]
# Use CMD to specify default arguments which can be overridden when container runs
CMD ["--ws_ip", "--host", "-l"]

