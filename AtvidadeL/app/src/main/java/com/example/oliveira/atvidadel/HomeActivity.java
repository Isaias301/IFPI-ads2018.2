package com.example.oliveira.atvidadel;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class HomeActivity extends AppCompatActivity {

    private int mCount = 0;
    private TextView mShowCount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        mShowCount = (TextView) findViewById(R.id.show_count);
    }

    public void mostrarToas(View view) {
        Toast toast = Toast.makeText(this, R.string.toast_message, Toast.LENGTH_SHORT);
        toast.show();
    }


    public void countUp(View view) {
        mCount ++;
        if(mShowCount != null){
            mShowCount.setText(Integer.toString(mCount));
        }
    }
}

