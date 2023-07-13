# choosing base image from docker hub image for python#
FROM python:3.9-slim-bookworm
# setting a working directory #
WORKDIR /app
# copy requirement into working directory for dependency reasons,from local machine into image directory ,using the last dot to copy to app#
COPY requirement.txt .

# pip to install on the requirement for dependency#
RUN pip3 install --no-cache-dir -r requirement.txt
# copy all things inside the directory #
COPY . .
# set enviroment variable,where to run the prog #
ENV FLASK_RUN_HOST=0.0.0.0
# EXPOSE  port,tho the app is running on port 5000#
EXPOSE 5000
# to make the command to be running #
CMD ["flask", "run"]