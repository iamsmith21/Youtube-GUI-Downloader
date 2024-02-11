def downloadVideo(url):
    command = f"yt-dlp -x -o \"%(title)s.%(ext)s\" --audio-format \"m4a\" --audio-quality 0 --embed-thumbnail --embed-metadata  --verbose '{url}'"
    #print(command)
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break

            # Display live output in a text widget
            output_text.set(line.strip())
            output_entry.update_idletasks()

        # Check if the process completed successfully
        if process.returncode == 0:
            output_text.set("Audio Downloaded Successfully.")
        else:
            output_text.set(f"Error: {process.stderr.read().strip()}")
        #todo : add setoutput var
    except subprocess.CalledProcessError as e:
        output_text.set(f"Error: {e.output}")
