    UPDATE full_names
    SET status = short_names.status 
    FROM short_names JOIN full_names f ON split_part(f.name, '.', 1) = short_names.name
    WHERE short_names.name = split_part(full_names.name, '.', 1);
~~~
    UPDATE full_names
    SET status = short_names.status
    FROM short_names
    WHERE full_names.name ~ ('^' || short_names.name || '\.');