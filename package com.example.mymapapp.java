package com.example.mymapapp;

import androidx.fragment.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mapRef;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);

        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);

        if (mapFragment != null) {
            mapFragment.getMapAsync(this);
        } else {
            System.out.println("Map fragment is null... weird");
        }
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        this.mapRef = googleMap;
        mapRef.setMapType(GoogleMap.MAP_TYPE_SATELLITE);

        LatLng sydney = new LatLng(-34.0, 151.0);
        mapRef.addMarker(new MarkerOptions().position(sydney).title("Marker in Sydney"));
        mapRef.moveCamera(CameraUpdateFactory.newLatLngZoom(sydney, 14.5f));
    }
}